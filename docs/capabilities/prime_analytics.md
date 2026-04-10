# Prime Analytics (`prime_analytics`)

### What it does
Finds likely primes quickly from odd-number candidates.
Instead of using deterministic trial division ($O(\sqrt{N})$), which severely impacts latency on large integers, this task implements the **Miller-Rabin Primality Test**. This allows for extreme speedups while maintaining a mathematically provable confidence interval.

### Algorithm Details & Optimizations
The Python reference implementation (`chuck/tasks/prime_analytics/task.py`) relies on several optimizations to maximize average-case throughput:
1. **Pre-screening:** Instantly filters out numbers divisible by the first 25 primes.
2. **Odd-Number-Only Generation:** The dataset generator strictly produces odd numbers, effectively halving the required compute space.
3. **Deterministic Probabilities:** To ensure snapshot comparisons and regression checks remain meaningful, the Random Number Generator (RNG) used to select Miller-Rabin witnesses is seeded by the candidate number itself (`rng = Random(number)`). This guarantees reproducible results across different hardware and backends.

### Why this design:
* Much faster than exact primality for large batches.
* Accepts tiny error probability for strong speed gains.
* **Input:** Large sets of odd integer candidates.
* **Output:** `candidates`, `probable_primes`, `density`, `confidence`, `checksum`.

### CLI Usage
To benchmark this specific capability and test your active backend:

```bash
python -m chuck bench --task prime_analytics
```
### Implementation Example
For a complete, runnable Python snippet with expected inputs and outputs, please see our dedicated usage guide:
👉 **[Prime Analytics Example](docs/usage/prime_analytics_example.md)**

### Usage of AI
Tool used - Google Gemini
usage - to create README.md for particular parts for good usage of technical terms.
parts in which AI is used - Algorithm Details & Optimizations
