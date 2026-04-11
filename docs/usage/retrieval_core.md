# Usage Example: retrieval_core

`retrieval_core` is a probabilistic task used for document indexing and query estimation.

## Example Script

```python
from chuck.tasks.retrieval_core.task import solve, generate

# 1. Generate sample data (documents and queries)
payload = generate(count=100, seed=42)

# 2. Execute the retrieval solver
# The payload contains 'docs' and 'queries'
results = solve(payload)

# 3. View Probabilistic Results
print(f"Confidence: {results['confidence']}")
print(f"Query Hits: {results['query_hits']}")
print(f"Top Term: {results['top_term']}")