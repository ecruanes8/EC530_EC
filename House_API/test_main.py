from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app
import pytest

client = TestClient(app)  # Create a test client for the API

device = {
            "device_id": "1",
            "name": "Smart Light",
            "room_id": "101",
            "device_type": "light",
            "status": "off"
        }
# Sample test user
test_user = {
    "id": 80364748,
    "name": "Eve",
    "email": "ecruanes@bu.edu",
    "password": "password"
}

# Test creating a user
def test_create_user():
    response = client.post("/users/", json=test_user)
    assert response.status_code == 200  # HTTP 200 OK
    assert response.json()["id"] == test_user["id"]
    assert response.json()["name"] == test_user["name"]

# Test getting a user (valid ID)
def test_get_user():
    test_user = {"id": 80364748, "name": "Eve Cruanes", "email": "ecruanes@bu.edu", "password": "password"}
    
    # Ensure the user exists before fetching
    client.post("/users/", json=test_user)
    response = client.get(f"/users/{test_user['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == test_user['id']


# Test creating a house
def test_create_house():
    test_house = {
        "house_id": "8",
        "name": "Paradise",
        "address": "277 Bedford Ave, Brooklyn, NY 11211",
        "owner_id": "8",
        "rooms": []
    }
    response = client.post("/houses/", json=test_house)
    assert response.status_code == 200
    assert response.json()["house_id"] == "8"

# Test getting a house (valid ID)
def test_get_house():
    response = client.get("/houses/8")
    assert response.status_code == 200
    assert response.json()["house_id"] == "8"

def test_create_device(): 
        
        response = client.post("/devices/", json=device)

        assert response.status_code == 200
        assert response.json()["device_id"] == "1"
def test_get_device():
        client.post("/devices/", json=device)  # Create it first
        response = client.get("/devices/1")

        assert response.status_code == 200
        assert response.json()["device_id"] == "1"