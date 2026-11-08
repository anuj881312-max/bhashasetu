# Contributing to BhashaSetu

Thank you for helping make open-source maintenance more accessible.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[openai,dev]"
python -m pytest
```

An API key is not required for tests or `--dry-run` previews.

## Pull requests

- Explain the user problem and the smallest useful change.
- Add or update tests for behavior changes.
- Keep provider-specific code behind the provider boundary.
- Do not commit real issue contents, personal data, API keys, or generated private prompts.
- If changing a prompt contract, include before/after examples or fixtures.
- Run `python -m pytest` and `python -m compileall src`.

## Translations

Native-speaker review is welcome. Preserve commands, links, code, environment variable names, and product names. Please note dialect or terminology choices in the pull request.

## Code of conduct

Participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
