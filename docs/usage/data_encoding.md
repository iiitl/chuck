# Data Encoding Usage

The `data_encoding` task handles high-performance data compression and verification.

### Usage Example
Integrating the task into a Python workflow is straightforward:

```python
from chuck.tasks.data_encoding.task import generate, solve

# 1. Generate a test payload (size in bytes, seed)
payload = generate(8192, 42)

# 2. Execute the solver
results = solve(payload)

# 3. Access results
print(f"Ratio: {results['ratio']:.2f}")
print(f"Integrity: {results['roundtrip']}")