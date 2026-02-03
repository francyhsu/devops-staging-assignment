import requests

BASE_URL = "http://127.0.0.1:8000"

def test_user_journey():
    # Step 1: Health Check
    health = requests.get(f"{BASE_URL}/health")
    assert health.status_code == 200
    
    # Step 2: User Creation (Sending JSON body)
    user_data = {"username": "e2e_tester", "email": "e2e@uchicago.edu"}
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    
    # Step 3: Verify Success
    assert response.status_code == 200
    assert "successfully" in response.json()["message"]
