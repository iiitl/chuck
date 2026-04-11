# prime_analytics : Examples & Usage
This benchmark evaluates computational throughput by calculating prime numbers and performing primality tests on a generated dataset.
## CLI Benchmark
### Input
You can use following command to benchmark your system on this task.
#### Bash:
```bash
python -m chuck bench --task prime_analytics
```
### Output
```text
Benchmark summary:
- prime_analytics: 0.024510s on size 1000 (upper_limit=1000)
```
## Usage in Code
To modify or use benchmark in your own code you can import `TASK_SPEC` and `solve_with_backend` functions from `chuck.tasks.prime_analytics` and `chuck.native_bindings`.
- `TASK_SPEC` config object contains the metadata and data generator for the task.
- `solve_with_backend` handles logic switching between Python and C++.
### Example
This script displays JSON result data followed by time taken:
#### Python Script
```python
import time
from chuck.native_bindings import solve_with_backend
from chuck.tasks.prime_analytics import TASK_SPEC

payload = TASK_SPEC.generator(10000, 42) # (upper_limit, seed)

# Task Execution and recording start and end times.
st_time = time.perf_counter()
result = solve_with_backend(task=TASK_SPEC, payload=payload, backend="python")
ed_time = time.perf_counter()

print(f"{result}, took time: {ed_time - st_time}")
```
#### Output
```text
{'candidates': 10000, 'probable_primes': 1355, 'prime_density_estimate': 0.1355, 'checksum': 715086865, 'probabilistic': True, 'confidence': 0.9961, 'backend': 'python'}, took time: 0.02887306400043599
```
