import json

from bhashasetu.cli import main


def test_dry_run_never_includes_a_secret(tmp_path, capsys):
    issue = tmp_path / "issue.json"
    issue.write_text(
        json.dumps(
            {
                "title": "Login fails",
                "body": "The token is sk-abcdefghijklmnopqrstuvwxyz123456",
            }
        ),
        encoding="utf-8",
    )
    assert main(["triage", "--file", str(issue), "--dry-run"]) == 0
    output = capsys.readouterr().out
    assert "REDACTED:openai_api_key" in output
    assert "sk-abcdefghijklmnopqrstuvwxyz123456" not in output
    assert '"mode": "dry-run"' in output
