# Data Encoding Usage

The `data_encoding` task handles high-performance data compression and verification.

### Usage Example
Integrating the task into a Python workflow is straightforward:

```python
from chuck.tasks.data_encoding.task import generate, solve

payload = generate(8192, 42)

results = solve(payload)

print(f"Ratio: {results['ratio']:.2f}")
print(f"Integrity: {results['roundtrip']}")