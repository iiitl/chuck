from chuck.tasks.prime_analytics.task import generate, solve

candidates = generate(count=10000, seed=42)

results = solve(candidates)

print(f"Candidates Tested: {results['candidates']}")
print(f"Probable Primes Found: {results['probable_primes']}")
print(f"Density Estimate: {results['prime_density_estimate']}")
print(f"Confidence Level: {results['confidence']}")
