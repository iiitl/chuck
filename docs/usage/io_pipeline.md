# io_pipeline : Examples & Usage
This benchmark simulates a data ingestion and transformation pipeline, measuring the throughput of moving data through various processing stages.
## CLI Benchmark
### Input
You can use following command to benchmark your system on this task.
#### Bash:
```bash
python -m chuck bench --task io_pipeline
```
### Output
```text
Benchmark summary:
- io_pipeline: 0.059077s on size 120000 (records=120000)
```
## Usage in Code
To modify or use benchmark in your own code you can import `TASK_SPEC` and `solve_with_backend` functions from `chuck.tasks.io_pipeline` and `chuck.native_bindings`.
- `TASK_SPEC` config object contains the metadata and data generator for the task.
- `solve_with_backend` handles logic switching between Python and C++.
### Example
This script displays JSON result data followed by time taken:
#### Python Script
```python
import time
from chuck.native_bindings import solve_with_backend
from chuck.tasks.io_pipeline import TASK_SPEC

payload = TASK_SPEC.generator(5000, 42) # (count, seed)

# Task Execution and recording start and end times.
st_time = time.perf_counter()
result = solve_with_backend(task=TASK_SPEC, payload=payload, backend="python")
ed_time = time.perf_counter()

print(f"{result}, took time: {ed_time - st_time}")
```
#### Output
```text
{'records': 5000, 'unique_pairs': 4950, 'total_value': 2501177, 'top_pair': 'acct_373|bucket_58', 'top_value': 1876, 'backend': 'python'}, took time: 0.002271692000249459
```
