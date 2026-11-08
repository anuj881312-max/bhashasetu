from bhashasetu.redaction import redact


def test_redacts_common_tokens_without_touching_normal_text():
    text = "hello sk-abcdefghijklmnopqrstuvwxyz123456 and ghp_abcdefghijklmnopqrstuvwxyz123456"
    cleaned, counts = redact(text)
    assert "sk-abcdefghijklmnopqrstuvwxyz123456" not in cleaned
    assert "ghp_abcdefghijklmnopqrstuvwxyz123456" not in cleaned
    assert counts["openai_api_key"] == 1
    assert counts["github_token"] == 1
    assert "hello" in cleaned


def test_private_key_block_is_redacted():
    text = "before\n-----BEGIN PRIVATE KEY-----\nsecret\n-----END PRIVATE KEY-----\nafter"
    cleaned, counts = redact(text)
    assert "secret" not in cleaned
    assert counts["private_key_block"] == 1
