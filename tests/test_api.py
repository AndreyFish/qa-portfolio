# test_api.py
import requests

def test_get_posts(api_base_url):
    response = requests.get(f"{api_base_url}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_user_by_id(api_base_url):
    response = requests.get(f"{api_base_url}/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert "name" in user   