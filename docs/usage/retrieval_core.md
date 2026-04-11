# Retrieval Core Task Usage
## What it does
The `retrieval_core` task acts like a mini search engine. It generates a bunch of fake text documents and then calculates how many times specific words appear across those documents. 
Instead of checking every single file, it uses math to sample just a few of them to estimate the final results. This is great for testing probabilistic search approximations.
## Example Script
Here's how you can run the task in Python to generate some fake data and solve it:
```python
from chuck.tasks import retrieval_core
# 1. Generate 100 fake documents
payload = retrieval_core.generate(count=100, seed=42)
# 2. Run the task to search through them
solution = retrieval_core.solve(payload)
# 3. Check the results
print(solution)