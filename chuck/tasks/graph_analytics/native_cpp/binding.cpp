#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <algorithm>
#include <cmath>
#include <map>
#include <string>
#include <vector>
#include <unordered_map>
#include <utility>

namespace py = pybind11;

py::dict solve(py::object payload_obj) {
    auto graph = payload_obj.cast<std::map<std::string, std::vector<std::string>>>();

    std::vector<std::string> nodes;
    nodes.reserve(graph.size());
    for (const auto& [node, _] : graph) {
        nodes.push_back(node);
    }
    std::sort(nodes.begin(), nodes.end());

    if (nodes.empty()) {
        py::dict output;
        output["node_count"] = py::int_(0);
        output["top_node"] = py::str("");
        output["top_score"] = py::float_(0.0);
        output["checksum"] = py::float_(0.0);
        return output;
    }

    const int n = static_cast<int>(nodes.size());

    // Fix: .reserve(n) ensures the load factor stays low, preventing hash collisions
    std::unordered_map<std::string, int> name_to_idx;
    name_to_idx.reserve(n);
    for (int i = 0; i < n; ++i) {
        name_to_idx[nodes[i]] = i;
    }

    std::vector<std::vector<int>> adj(n);
    for (int u = 0; u < n; ++u) {
        auto found = graph.find(nodes[u]);
        if (found != graph.end() && !found->second.empty()) {
            adj[u].reserve(found->second.size());
            for (const auto& target : found->second) {
                adj[u].push_back(name_to_idx.at(target));
            }
        }
    }

    constexpr int iterations = 16;
    constexpr double damping = 0.85;
    const double base = (1.0 - damping) / static_cast<double>(n);

    std::vector<double> rank(n, 1.0 / static_cast<double>(n));
    std::vector<double> new_rank(n, 0.0);

    for (int step = 0; step < iterations; ++step) {
        std::fill(new_rank.begin(), new_rank.end(), base);

        double dangling_share = 0.0;
        for (int u = 0; u < n; ++u) {
            if (adj[u].empty()) {
                dangling_share += damping * rank[u] / static_cast<double>(n);
                continue;
            }
            const double share = (damping * rank[u]) / static_cast<double>(adj[u].size());
            for (int v : adj[u]) {
                new_rank[v] += share;
            }
        }

        if (dangling_share > 0.0) {
            for (double& value : new_rank) {
                value += dangling_share;
            }
        }
        std::swap(rank, new_rank);
    }

    int top_idx = 0;
    double top_score = rank[0];
    for (int i = 1; i < n; ++i) {
        if (rank[i] > top_score || (std::abs(rank[i] - top_score) < 1e-15 && nodes[i] > nodes[top_idx])) {
            top_score = rank[i];
            top_idx = i;
        }
    }

    double checksum = 0.0;
    for (int i = 0; i < n; ++i) {
        checksum += static_cast<double>(i + 1) * rank[i];
    }

    py::dict output;
    output["node_count"] = py::int_(n);
    output["top_node"] = py::str(nodes[top_idx]);
    output["top_score"] = py::float_(std::round(top_score * 1000000.0) / 1000000.0);
    output["checksum"] = py::float_(std::round(checksum * 1000000.0) / 1000000.0);
    return output;
}

PYBIND11_MODULE(chuck_cpp_graph_analytics, m) {
    m.doc() = "C++ binding for chuck graph_analytics";
    m.def("solve", &solve);
}
