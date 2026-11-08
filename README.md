# BhashaSetu

**A privacy-first, Hindi-first AI assistant for open-source maintainers.**

BhashaSetu helps small and volunteer-led projects understand issues, improve documentation, and welcome contributors in Hindi and other languages. It creates **reviewable drafts**; it does not automatically merge code, close issues, or publish replies.

> Independent community project. BhashaSetu is not affiliated with or endorsed by OpenAI.

## Why this matters

Many open-source projects have good code but limited maintainer time. Contributors who are more comfortable in Hindi or another local language can also face a documentation and communication barrier. BhashaSetu combines language access with conservative maintainer workflows:

- issue triage with a fixed, inspectable JSON contract;
- beginner-friendly explanations of code and issues;
- Markdown translation that preserves commands, links, and code blocks;
- secret redaction before model input;
- offline prompt previews and a human-review-first policy;
- an optional Codex CLI workflow for repository changes.

## Current status

Alpha. The command-line MVP and tests are included. GitHub API automation, a larger evaluation set, and additional Indian languages are planned and tracked in [`GRANT_PROPOSAL.md`](GRANT_PROPOSAL.md).

## Quick start

Requires Python 3.10 or newer.

```bash
git clone https://github.com/YOUR-USERNAME/bhashasetu.git
cd bhashasetu
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
python -m pip install -e ".[openai,dev]"
```

Preview a request without sending anything to a model:

```bash
bhashasetu triage --file examples/issue.json --dry-run
```

Run a real request after setting your own API key:

```bash
export OPENAI_API_KEY="your-key"
bhashasetu triage --file examples/issue.json --language hi
```

The default model is `gpt-4o-mini`; override it with `--model` or `BHASHASETU_MODEL`. The model name is deliberately configurable so the community can evaluate newer or lower-cost models without changing application code.

Other commands:

```bash
# Explain code or an issue for a beginner contributor
bhashasetu explain --file src/bhashasetu/redaction.py --language hi

# Translate prose while preserving Markdown and code
bhashasetu translate --file README.md --to hi --output docs/hi/README.generated.md

# Produce a reviewable prompt for Codex CLI
bhashasetu codex-prompt \\
  --task "Add a GitHub Action that runs the offline safety tests" \\
  --file AGENTS.md
```

## Safety model

BhashaSetu is intentionally not an autonomous GitHub bot.

1. Input is treated as untrusted repository data.
2. Known API keys, GitHub tokens, AWS secret values, and private-key blocks are redacted before a provider call.
3. The request can be inspected with `--dry-run`.
4. The output is a draft and must be reviewed by a human.
5. Security reports should be handled through a private channel; the public suggested reply avoids exploit details.

Redaction is a defense-in-depth feature, not a guarantee. Do not send material that you are not authorized to process.

## Codex CLI workflow

`AGENTS.md` contains repository-specific instructions for safe coding work. The optional `scripts/codex_review.sh` demonstrates a read-only review workflow. It is kept separate from the OpenAI API adapter so the project remains useful even when Codex CLI is not installed.

Typical workflow:

```bash
# Inspect a change without giving the coding agent write access
bash scripts/codex_review.sh "Review the current diff for security and missing tests"
```

Always review generated changes and run the test suite locally. CLI flags can vary by Codex version; consult the installed Codex CLI help if needed.

## Development

```bash
python -m pytest
python -m compileall src
ruff check .  # optional
```

Contributions are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md), and [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Roadmap

- **v0.2:** GitHub issue export/import with explicit dry-run mode; Hindi, Bengali, Marathi, and Tamil prompt fixtures.
- **v0.3:** Maintainer-approved GitHub Action that posts no comments by default and emits artifacts for review.
- **v0.4:** Public evaluation dashboard covering language fidelity, label accuracy, secret-redaction recall, and maintainer time saved.
- **Later:** Pluggable providers and local-model support so communities can choose their privacy/cost trade-offs.

## License

MIT. See [`LICENSE`](LICENSE).
