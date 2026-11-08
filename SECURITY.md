# Security policy

## Scope

BhashaSetu processes repository content and may send redacted text to a configured model provider. It is not a secure vault and should not be used to process material that you are not authorized to share.

## Safe usage

- Never put production credentials in issue text or test fixtures.
- Use `--dry-run` to inspect the redacted request.
- Review drafts before publishing them.
- Do not use the public triage command for confidential vulnerability details; use the project's private security channel.
- Keep `OPENAI_API_KEY` in an environment variable or secret manager, never in the repository.

Redaction is defense in depth. It does not prove that arbitrary secrets or personal data have been removed.

## Reporting a vulnerability

Please do not open a public issue for an undisclosed vulnerability. Contact **[maintainer security contact]** with a clear description, reproduction steps, impact, and a safe contact method. We aim to acknowledge reports within seven days.
