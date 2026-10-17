from agent import ask_agent


def test_agent_returns_answer():
    result = ask_agent("What is the total sales?")
    assert isinstance(result, str)
    assert len(result) > 0


def test_agent_handles_sop_question():
    result = ask_agent("What is the sales return policy?")
    assert isinstance(result, str)
    assert len(result) > 0