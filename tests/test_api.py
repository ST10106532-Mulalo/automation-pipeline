import requests
import pytest

# This is the URL of my API that is running
API_URL = "http://127.0.0.1:8000"

def test_health_check():
    # I am testing if the API is running
    response = requests.get(f"{API_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "API is running"

def test_save_test_result():
    # I am testing if I can save a test result
    test_data = {
        "test_name": "automated_test_1",
        "passed": True,
        "duration_ms": 150
    }
    
    response = requests.post(f"{API_URL}/results", json=test_data)
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_save_failing_test():
    # I am testing if I can save a failing test result
    test_data = {
        "test_name": "failing_test_1",
        "passed": False,
        "duration_ms": 200,
        "error_message": "This test failed because of a bug"
    }
    
    response = requests.post(f"{API_URL}/results", json=test_data)
    assert response.status_code == 200
    assert response.json()["status"] == "success"