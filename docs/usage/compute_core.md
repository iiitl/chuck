# compute_core: Examples & Usage

The `compute_core` task runs dense, CPU-heavy numeric kernels (specifically blocked/tiled matrix multiplication) to benchmark mathematical throughput and cache efficiency.


## CLI Benchmark

In this example we will be using the built-in CLI runner. This will automatically generate a deterministic 64x64 matrix using a custom seed, execute the fastest available backend (C++ backend if available, otherwise Python), and return the time taken.

Run the command below to benchmark your CPU on this task:

```bash
python -m chuck bench --task compute_core
```
