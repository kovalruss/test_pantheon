import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client(admin_user) -> APIClient:
    client = APIClient()
    return client
