# compute_core: Examples & Usage

The `compute_core` task runs dense, CPU-heavy numeric kernels (specifically blocked/tiled matrix multiplication) to benchmark mathematical throughput and cache efficiency.


## CLI Benchmark

The below command can be used to benchmark your system on this task:

```bash
python -m chuck bench --task compute_core
```

## Usage in Code

If you want to use or modify this benchmark in your own code, you will need to import `TASK_SPEC` from `compute_core` and `solve_with_backend` function from the `native_bindings` file.

For example, this snippet displays the time taken along with JSON result data:
```python
from chuck.native_bindings import solve_with_backend
from chuck.tasks.compute_core import TASK_SPEC
import time

payload = TASK_SPEC.generator(64, 117)
st_time = time.perf_counter()
result = solve_with_backend(task=TASK_SPEC, payload=payload, backend="python")
ed_time = time.perf_counter()
print(f"{result}, took time: {ed_time - st_time}")
```

Output:
```text
{'size': 64, 'trace': 83341, 'checksum': 5344296, 'backend': 'python'}, took time: 0.01829049299703911
```
