from __future__ import annotations

from random import Random
from typing import Any

from ...common import TaskSpec
import numpy as np


def generate(size: int, seed: int) -> dict[str, Any]:
    rng = Random(seed)
    left = [[rng.randrange(0, 10) for _ in range(size)] for _ in range(size)]
    right = [[rng.randrange(0, 10) for _ in range(size)] for _ in range(size)]
    return {"left": left, "right": right, "block_size": max(2, min(16, size // 4 or 2))}


def solve(payload: dict[str, Any]) -> dict[str, Any]:
     left = np.asarray(payload["left"], dtype=np.int64)
     right = np.asarray(payload["right"], dtype=np.int64)
     size = len(left)
     result = np.matmul(left, right)
     trace = int(np.trace(result, dtype=np.int64))
     checksum = int(np.sum(result, dtype=np.int64))
    return {"size": size, "trace": trace, "checksum": checksum}


TASK_SPEC = TaskSpec("compute_core", generate, solve, 16, 64)
