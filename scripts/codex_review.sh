#!/usr/bin/env bash
set -euo pipefail

if ! command -v codex >/dev/null 2>&1; then
  echo "Codex CLI is required. Install it, then run this script again." >&2
  exit 1
fi

TASK="${*:-Review the current changes for correctness, security, tests, and documentation. Do not edit files.}"

bhashasetu codex-prompt --task "$TASK" --file README.md > /tmp/bhashasetu-codex-prompt.json
python - <<'PY'
import json
from pathlib import Path
payload = json.loads(Path('/tmp/bhashasetu-codex-prompt.json').read_text())
print(payload['prompt'])
PY

codex exec --sandbox read-only --ask-for-approval on-request "$TASK"
