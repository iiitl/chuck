# prime_analytics (`prime_analytics`)

What it does: Finds likely primes quickly from odd-number candidates.
Instead of using deterministic trial division ($O(\sqrt{N})$), which severely impacts latency on large integers, this task implements the **Miller-Rabin Primality Test**.

### Algorithm Details & Optimizations
The Python reference implementation (`chuck/tasks/prime_analytics/task.py`) relies on several optimizations to maximize average-case throughput:
1. **Pre-screening:** Instantly filters out numbers divisible by the first 10 primes.
2. **Odd-Number-Only Generation:** The dataset generator strictly produces odd numbers, effectively halving the required compute space.
3. **Deterministic Probabilities:** To ensure snapshot comparisons and regression checks remain meaningful, the Random Number Generator (RNG) used to select Miller-Rabin witnesses is seeded by the candidate number itself (`rng = Random(number)`). This guarantees reproducible results across different hardware and backends.

### Performance vs. Reliability Trade-off (Blast Radius)
Because this task is **probabilistic**, it trades absolute certainty for speed.
* **Rounds:** The solver executes `4` rounds of Miller-Rabin testing per candidate.
* **Confidence Score:** A composite number has at most a $1/4$ chance of passing a single round. Therefore, the theoretical confidence level for a positively identified prime is `~0.996` ($1.0 - 0.25^4$).
* **Blast Radius:** Approximately 4 out of every 1,000 composite numbers (pseudoprimes) may be falsely identified as prime. For large-scale data density estimation, this margin of error is fully acceptable.

### Why this design:
- Much faster than exact primality for large batches.
- Accepts tiny error probability for strong speed gains.

This allows for extreme speedups while maintaining a mathematically provable confidence interval.

Input: Large sets of odd integer candidates.

Output: `candidates`, `probable_primes`, `density`, `confidence`, `checksum`.

### CLI Usage
To benchmark this specific capability and test your active backend:

```bash
python -m chuck bench --task prime_analytics

### Python Quick Start
You can easily import tasks directly into your own workflows. Here is an example using the probabilistic prime number solver:

```python
from chuck.tasks.prime_analytics.task import generate, solve

candidates = generate(count=10000, seed=42)
results = solve(candidates)

print(f"Primes Found: {results['probable_primes']} (Confidence: {results['confidence']})")
