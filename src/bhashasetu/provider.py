"""Optional OpenAI Responses API adapter."""

from __future__ import annotations

import os
from typing import Any


class ProviderError(RuntimeError):
    """A user-facing error from the model provider."""


class OpenAIProvider:
    """Minimal adapter kept separate so offline workflows remain usable."""

    def __init__(self, model: str = "gpt-4o-mini", api_key: str | None = None) -> None:
        key = api_key or os.getenv("OPENAI_API_KEY")
        if not key:
            raise ProviderError(
                "OPENAI_API_KEY is not set. Use --dry-run for an offline preview or set the key."
            )
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise ProviderError(
                "The OpenAI SDK is not installed. Run: pip install -e '.[openai]'"
            ) from exc
        self._client: Any = OpenAI(api_key=key)
        self.model = model

    def complete(self, system: str, user: str) -> str:
        """Generate text with the Responses API and return only model text."""

        try:
            response = self._client.responses.create(
                model=self.model,
                instructions=system,
                input=user,
            )
            text = getattr(response, "output_text", None)
            if not text:
                raise ProviderError("The model returned no text output.")
            return str(text).strip()
        except ProviderError:
            raise
        except Exception as exc:  # SDK errors vary by version/provider
            raise ProviderError(f"OpenAI request failed: {exc}") from exc
