# utils
"""Miscellaneous utility helpers for the stock service."""


def slugify(text):
    """Return a lowercase, dash-separated slug of `text`."""
    slug = "".join(ch if ch.isalnum() else "-" for ch in str(text).lower())
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def coalesce(*values, default=None):
    """Return the first truthy value, or `default` if none are truthy."""
    for value in values:
        if value:
            return value
    return default


def flatten(items):
    """Flatten one level of nested lists/tuples."""
    result = []
    for item in items:
        if isinstance(item, (list, tuple)):
            result.extend(item)
        else:
            result.append(item)
    return result


def safe_divide(numerator, denominator, default=0.0):
    """Divide without raising on a zero denominator."""
    return numerator / denominator if denominator else default
