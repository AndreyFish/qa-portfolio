import pytest

@pytest.fixture
def base_url():
    # Example base URL for public demo API
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def client():
    # simple requests-style client placeholder
    import requests
    return requests