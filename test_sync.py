import pytest
from unittest.mock import patch
from dentally_client import push_contact_to_dentally
from models import Contact

@pytest.fixture
def sample_contact():
    return Contact(id="1", first_name="Alice", last_name="Smith", email="alice@example.com")

def test_push_contact_success(sample_contact):
    with patch("httpx.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.raise_for_status = lambda: None

        result = push_contact_to_dentally(sample_contact)
        assert result is True
        mock_post.assert_called_once_with(
            "http://localhost:8001/customers", json=sample_contact.model_dump()
        )

def test_push_contact_failure(sample_contact):
    with patch("httpx.post") as mock_post:
        mock_post.return_value.status_code = 400
        mock_post.return_value.raise_for_status.side_effect = Exception("Bad Request")

        result = push_contact_to_dentally(sample_contact)
        assert result is False
        mock_post.assert_called_once_with(
            "http://localhost:8001/customers", json=sample_contact.model_dump()
        )