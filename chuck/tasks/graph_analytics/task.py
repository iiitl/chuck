from __future__ import annotations

import numpy as np
from random import Random
from typing import Any

from ...common import TaskSpec, round6


def generate(node_count: int, seed: int) -> dict[str, list[str]]:
    rng = Random(seed)
    nodes = [f"n{index:04d}" for index in range(node_count)]
    graph: dict[str, list[str]] = {}
    for index, node in enumerate(nodes):
        degree = 2 + rng.randrange(3)
        edges = {nodes[(index + 1) % node_count]}
        while len(edges) < degree:
            edges.add(nodes[rng.randrange(node_count)])
        graph[node] = sorted(edges)
    return graph


def solve(graph: dict[str, list[str]], iterations: int = 16, damping: float = 0.85) -> dict[str, Any]:
    nodes = sorted(graph)
    n = len(nodes)
    if n == 0:
        return {"node_count": 0, "top_node": "", "top_score": 0.0, "checksum": 0.0}

    node_to_idx = {node: i for i, node in enumerate(nodes)}

    src_list = []
    dst_list = []
    out_degrees = np.zeros(n)

    for i, node in enumerate(nodes):
        neighbors = graph[node]
        out_degrees[i] = len(neighbors)
        for neighbor in neighbors:
            src_list.append(i)
            dst_list.append(node_to_idx[neighbor])

    src_indices = np.array(src_list)
    dst_indices = np.array(dst_list)

    ranks = np.full(n, 1.0 / n)
    teleport_base = (1.0 - damping) / n

    for _ in range(iterations):
        new_ranks = np.full(n, teleport_base)
        contributions = (ranks[src_indices] / out_degrees[src_indices]) * damping
        np.add.at(new_ranks, dst_indices, contributions)
        ranks = new_ranks

    top_idx = np.argmax(ranks)
    top_node = nodes[top_idx]
    checksum = np.sum(np.arange(1, n + 1) * ranks)

    return {
        "node_count": n,
        "top_node": top_node,
        "top_score": round6(ranks[top_idx]),
        "checksum": round6(float(checksum)),
    }


TASK_SPEC = TaskSpec("graph_analytics", generate, solve, 48, 1_000)
