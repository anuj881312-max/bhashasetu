# Open-source grant proposal: BhashaSetu

> This is a working proposal template, not an official application. Replace the identity and repository placeholders before submitting.

## One-line summary

BhashaSetu is a privacy-first, Hindi-first maintainer assistant that uses OpenAI models and Codex CLI to help volunteer-led open-source projects triage issues, translate documentation, and welcome contributors without surrendering human review.

## Applicant

- Maintainer: **[anuj kumar rawat ]**
- Public repository: **[https://github.com/anuj881312-max/bhashasetu]**
- Contact: **[anujrawat881213@gmail.com]**
- Relevant experience: **[This is my first public open-source project. I am building BhashaSetu to help open-source maintainers and Indian-language contributors.]**

## Problem

Maintainers of small projects spend significant time repeating the same work: understanding incomplete issues, writing welcoming replies, and keeping documentation current. The language barrier adds friction for contributors who are more comfortable in Hindi and other Indian languages. Existing AI bots can be difficult to audit and may post incorrect or sensitive content automatically.

## Proposed solution

BhashaSetu makes AI assistance a local, inspectable workflow:

1. A maintainer exports or pastes an issue, code file, or Markdown document.
2. BhashaSetu redacts common credentials and produces a model request that can be previewed.
3. An OpenAI model returns a structured triage result or a translation/explanation draft.
4. A human maintainer reviews, edits, and decides whether to publish anything.
5. Codex CLI can be used for repository-level changes under the instructions in `AGENTS.md`, with tests and review required.

The MVP already includes a Python CLI, provider boundary, prompt contracts, redaction tests, offline mode, documentation, and CI. The grant would fund reliability, language evaluation, and careful GitHub integration—not a closed hosted service.

## Why OpenAI models and Codex CLI

- The Responses API gives the project one small provider boundary with configurable models.
- Structured prompts make issue triage easier to test and compare.
- Codex CLI is useful for repository-aware, test-driven maintenance work when a maintainer explicitly approves changes.
- The project keeps prompts, tests, and safety rules in the public repository so the community can audit how the tools are used.

## Requested support

**Requested: up to $15,000 in API credits over six months.** The exact amount can be adjusted after a small pilot. Credits would be used for development, evaluation, and opt-in community pilots; they would not be used to train a private model or build a paywalled API.

### Planned usage controls

- per-run model and token limits;
- a local `--dry-run` preview;
- redaction before provider calls;
- no automatic public GitHub comments or merges;
- opt-in pilot repositories with documented consent;
- monthly public usage and evaluation reports;
- a kill switch and provider-independent offline tests.

## Six-month milestones

### Month 1: harden the foundation

- Add golden fixtures for English and Hindi issue triage.
- Expand redaction tests, including false-positive review.
- Add request-size limits and a local configuration file.
- Document threat model and responsible-use guidance.

**Deliverable:** v0.2 CLI with reproducible offline tests.

### Months 2–3: language and maintainer evaluation

- Add reviewed fixtures for Hindi, Bengali, Marathi, and Tamil.
- Recruit 5–10 volunteer projects for opt-in feedback.
- Measure label accuracy, translation fidelity, human edit rate, and time saved.
- Publish anonymized evaluation methodology and results.

**Deliverable:** public evaluation set and first pilot report.

### Months 4–5: review-first GitHub integration

- Build an exporter that reads issues without posting changes.
- Add an artifact-based GitHub Action: output is a downloadable draft, never an automatic comment.
- Add permissions documentation and integration tests with mocked GitHub responses.
- Use Codex CLI for test-driven repository maintenance, with human review.

**Deliverable:** v0.3 Action and integration documentation.

### Month 6: release and sustainability

- Fix pilot issues and publish a stable release candidate.
- Publish a final impact report and a credits/usage summary.
- Create a contributor onboarding guide and maintainer governance notes.
- Document a path to pluggable providers and local models.

**Deliverable:** release candidate, public report, and next-year roadmap.

## Success metrics

- 10 pilot repositories and at least 200 anonymized evaluation fixtures.
- At least 80% of triage drafts judged useful without factual invention in human review.
- At least 90% preservation of commands, links, and code blocks in translation fixtures.
- 100% of seeded test secrets detected by the supported redaction suite.
- 25% median reduction in time spent preparing first responses, measured by opt-in maintainers.
- At least 20 external contributors or issue participants during the pilot.

Metrics will be reported with limitations; the project will not claim that model output is correct merely because it is fluent.

## Open-source commitments

All application code, prompts, safety rules, tests, evaluation methodology, and pilot documentation will remain public under the MIT license or a clearly documented compatible license. User-provided issue content will not be committed to the repository. Any published fixture will be synthetic, anonymized, or shared with explicit permission.

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Incorrect triage or translation | Draft-only output, structured contracts, human review, golden fixtures |
| Secret or personal-data leakage | Redaction, dry-run, warnings, opt-in pilot, no automatic posting |
| Bias or exclusion in language output | Native-speaker review, community feedback, error reporting |
| API cost growth | Model selection, request limits, caching only with consent, public usage report |
| Overreliance on one vendor | Provider boundary, offline mode, roadmap for local/pluggable models |

## Sustainability

After the pilot, the project can continue as a community-maintained CLI with optional provider adapters. The core safety and offline functionality will remain free and open source. Governance, release checklists, and evaluation fixtures are designed so contributors can improve the project without access to paid infrastructure.
