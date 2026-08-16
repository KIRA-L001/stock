# metrics
"""Lightweight metrics collection helpers for the stock service."""

import time
from collections import deque


class LatencyRecorder:
    """Tracks rolling latency samples and exposes summary statistics."""

    def __init__(self, window=100):
        self.window = window
        self._samples = deque(maxlen=window)

    def record(self, seconds):
        self._samples.append(float(seconds))

    def count(self):
        return len(self._samples)

    def mean(self):
        if not self._samples:
            return 0.0
        return sum(self._samples) / len(self._samples)

    def p95(self):
        if not self._samples:
            return 0.0
        ordered = sorted(self._samples)
        idx = max(0, int(round(0.95 * (len(ordered) - 1))))
        return ordered[idx]


def format_ms(seconds):
    """Render a duration in seconds as a human millisecond string."""
    return f"{seconds * 1000:.1f}ms"


def now_ms():
    return time.time() * 1000
