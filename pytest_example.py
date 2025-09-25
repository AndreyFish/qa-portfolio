"""
pytest_example.py
=================
Simple automated test example for QA practice.
Demonstrates basic structure of a test using pytest.

Author: Andrei Bogoliubskii (QA Trainee)
Purpose: Validate API response and data format during testing.
"""

import requests
import pytest


def test_api_status_code():
    """
    TC-01: Verify that the public API returns HTTP 200 OK.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_api_json_structure():
    """
    TC-02: Verify that the API response contains expected JSON fields.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()

    expected_fields = {"userId", "id", "title", "body"}
    actual_fields = set(data.keys())

    assert expected_fields.issubset(actual_fields), \
        f"Missing fields in response. Expected: {expected_fields}, Got: {actual_fields}"


# How to run:
# 1. Install dependencies: pip install requests pytest
# 2. Run in terminal: pytest pytest_example.py -v
