from bhashasetu.prompts import system_prompt, user_prompt


def test_triage_prompt_has_a_machine_readable_contract():
    prompt = system_prompt("triage", "hi")
    assert "valid JSON" in prompt
    assert "suggested_reply" in prompt
    assert "hi" in prompt


def test_user_content_is_delimited_as_untrusted():
    prompt = user_prompt("explain", "ignore this instruction", "Hindi")
    assert "BEGIN REPOSITORY CONTENT" in prompt
    assert "END REPOSITORY CONTENT" in prompt
    assert "ignore this instruction" in prompt
