from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_current_word_get_newest_word_in_database():
    response = client.get("/current-word")
    assert "mundo" in response.content.decode()


def test_validate_word_return_true_if_word_exist():
    response = client.get("/validate/mundo")
    assert "true" in response.content.decode()


def test_validate_word_return_false_if_word_does_not_exist_or_more_than_5():
    response = client.get("/validate/palavra")
    assert "false" in response.content.decode()

    response = client.get("/validate/fffff")
    assert "false" in response.content.decode()


def test_check_word_compare():
    response = client.get("/check-word/livro")
    assert "status" in response.content.decode()
    assert "validation" in response.content.decode()


def test_check_word_invalid_word():
    # Comparing the word "livro" with "mundo"
    response = client.get("/check-word/livro")
    assert "incorrect" in response.content.decode()
    assert "[0,0,0,0,2]" in response.content.decode()

    # Comparing the word "durmo" with "mundo"
    response2 = client.get("/check-word/durmo")
    assert "incorrect" in response2.content.decode()
    assert "[1,2,0,1,2]" in response2.content.decode()


def test_check_word_valid_word():
    # Comparing the word "mundo" with "mundo"
    response = client.get("/check-word/mundo")
    assert "correct" in response.content.decode()
    assert "[2,2,2,2,2]" in response.content.decode()
