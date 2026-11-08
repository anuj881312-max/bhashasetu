"""Small, conservative secret redaction layer.

BhashaSetu never sends the unredacted source text to a model. This module is
intentionally dependency-free so it can run before an optional model SDK is
installed.
"""

from __future__ import annotations

import re
from collections.abc import Iterable


_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("openai_api_key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("github_token", re.compile(r"\b(?:ghp|gho|ghs|ghu)_[A-Za-z0-9]{20,}\b")),
    ("github_pat", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    (
        "aws_secret",
        re.compile(r"(?i)(aws_secret_access_key\s*[:=]\s*[\"']?)[A-Za-z0-9/+=]{20,}"),
    ),
    (
        "private_key_block",
        re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", re.S),
    ),
)


def redact(text: str) -> tuple[str, dict[str, int]]:
    """Return redacted text and a count of each detected secret type."""

    counts: dict[str, int] = {}
    result = text
    for label, pattern in _PATTERNS:
        replacement = f"[REDACTED:{label}]"
        result, count = pattern.subn(replacement, result)
        if count:
            counts[label] = count
    return result, counts


def redact_many(parts: Iterable[str]) -> tuple[list[str], dict[str, int]]:
    """Redact several strings while combining their detection counts."""

    redacted: list[str] = []
    total: dict[str, int] = {}
    for part in parts:
        cleaned, counts = redact(part)
        redacted.append(cleaned)
        for label, count in counts.items():
            total[label] = total.get(label, 0) + count
    return redacted, total
