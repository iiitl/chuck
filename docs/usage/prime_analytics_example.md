# Prime Analytics Usage Example

This document provides a standalone example of how to import and run the `prime_analytics` capability in your Python scripts.

## Example Snippet (Input)
The following script generates a batch of odd-number candidates and runs the Miller-Rabin probabilistic primality test on them.

```python
from chuck.tasks.prime_analytics.task import generate, solve

candidates = generate(count=10000, seed=42)
results = solve(candidates)

print(f"Candidates Tested: {results['candidates']}")
print(f"Probable Primes Found: {results['probable_primes']}")
print(f"Density Estimate: {results['prime_density_estimate']}")
print(f"Confidence Level: {results['confidence']}")
```
### Expected Output:

Candidates Tested: 10000
Probable Primes Found: 924
Density Estimate: 0.0924
Confidence Level: 0.9961

### Usage of AI
Tool used - Google Gemini
usage - To create README.md for particular parts for good usage of technical terms.
parts in which AI is used - Prime Analytics Usage Example, Example Snippet
