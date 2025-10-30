# conftest.py
import pytest
import requests

@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com"   
import pytest
import requests

#@pytest.fixture
def base_url():
    return "https://bookstore-demo.herokuapp.com"   
