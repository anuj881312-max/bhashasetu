# Evaluation plan

BhashaSetu should be evaluated as a maintainer tool, not only as a language-model demo.

## Offline fixture categories

- issue type: bug, feature, docs, question, security, other;
- language: English, Hindi, Bengali, Marathi, Tamil;
- issue quality: complete, ambiguous, duplicate-like, emotionally frustrated;
- safety: seeded tokens, private-key blocks, and personal-data placeholders;
- documentation: Markdown links, shell commands, code blocks, tables, and inline code.

## Measures

1. **Triage usefulness:** two maintainers independently score whether labels, priority, questions, and draft reply are useful.
2. **Factuality:** reviewers mark claims that are not supported by the fixture.
3. **Language fidelity:** native speakers score meaning, tone, and terminology.
4. **Structure preservation:** automated checks compare links, code fences, commands, and environment variables.
5. **Privacy:** seeded secrets must never appear in the provider request or generated logs.
6. **Human effort:** pilot maintainers record time to prepare a first response with and without a draft.

Results should include sample size, model name, prompt version, failure cases, and reviewer limitations. No result should be presented as a guarantee for every repository.
