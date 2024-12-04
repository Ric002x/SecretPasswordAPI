import pytest
from fastapi.testclient import TestClient

from app import create_api


class TestBaseApplication():

    @pytest.fixture
    def app(self):
        self.application = create_api()
        yield self.application

    @pytest.fixture
    def client(self, app):
        return TestClient(self.application)

    def test_root_url_return_404(self, client):
        response = client.get("/")
        assert response.status_code == 404

    def test_current_word_get_newest_word_in_database(self, client):
        response = client.get("/current-word")
        assert "mundo" in response.content.decode()

    def test_validate_word_return_true_if_word_exist(self, client):
        response = client.get("/validate/mundo")
        assert "true" in response.content.decode()

    def test_validate_word_return_false_if_is_invalid(self, client):
        response = client.get("/validate/palavra")
        assert "false" in response.content.decode()

        response = client.get("/validate/fffff")
        assert "false" in response.content.decode()

    def test_check_word_compare(self, client):
        response = client.get("/check-word/livro")
        assert "status" in response.content.decode()
        assert "validation" in response.content.decode()

    def test_check_word_invalid_word(self, client):
        # Comparing the word "livro" with "mundo"
        response = client.get("/check-word/livro")
        assert "incorrect" in response.content.decode()
        assert "[0,0,0,0,2]" in response.content.decode()

        # Comparing the word "durmo" with "mundo"
        response2 = client.get("/check-word/durmo")
        assert "incorrect" in response2.content.decode()
        assert "[1,2,0,1,2]" in response2.content.decode()

    def test_check_word_valid_word(self, client):
        # Comparing the word "mundo" with "mundo"
        response = client.get("/check-word/mundo")
        assert "correct" in response.content.decode()
        assert "[2,2,2,2,2]" in response.content.decode()
