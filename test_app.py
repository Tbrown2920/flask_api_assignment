"""
Program: Flask Testing Suite
Description: Validates server execution routes and status codes using pytest.
Author: Teresa Brown
References: Code structure optimized with debugging assistance from Gemini AI.
"""
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    # Test GET endpoint with no parameters
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {"greeting": "Hello, World!"}

    # Test GET endpoint with explicit name parameter
    response = client.get('/hello?name=Teresa')
    assert response.status_code == 200
    assert response.get_json() == {"greeting": "Hello, Teresa!"}

def test_sum_endpoint_success(client):
    # Test valid POST list processing math operations
    response = client.post('/sum', json={"numbers": [1, 2, 3, 4]})
    assert response.status_code == 200
    assert response.get_json() == {"sum": 10.0}

def test_sum_endpoint_errors(client):
    # Test error fallback rule for missing key fields (HTTP 400)
    response = client.post('/sum', json={})
    assert response.status_code == 400
    
    # Test error fallback rule for invalid data parameters
    response = client.post('/sum', json={"numbers": ["invalid_text", 2]})
    assert response.status_code == 400