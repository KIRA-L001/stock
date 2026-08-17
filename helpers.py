# helpers
"""Generic helper utilities used across the stock service."""

import time


def chunked(items, size):
    """Yield successive `size`-length chunks from `items`."""
    if size <= 0:
        raise ValueError("size must be positive")
    for i in range(0, len(items), size):
        yield items[i:i + size]


def retry(attempts=3, backoff=0.1):
    """Decorator that retries a callable on exception with linear backoff."""
    def decorator(fn):
        def wrapper(*args, **kwargs):
            delay = backoff
            for _ in range(attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception:
                    time.sleep(delay)
                    delay += backoff
            return fn(*args, **kwargs)
        return wrapper
    return decorator


def memoize(fn):
    """Cache `fn`'s results, keyed by positional arguments."""
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return wrapper
