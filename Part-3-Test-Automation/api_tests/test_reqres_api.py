import os
import requests


BASE_URL = "https://reqres.in/api"

API_KEY = os.getenv("REQRES_API_KEY")

HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}


def test_get_users_success():
    """
    AT-09
    GET users successfully
    """

    response = requests.get(
        f"{BASE_URL}/users?page=2",
        headers=HEADERS,
        timeout=10
    )

    # Status code assertion
    assert response.status_code == 200

    body = response.json()

    # Response body shape assertions
    assert isinstance(body, dict)

    assert "page" in body
    assert "per_page" in body
    assert "total" in body
    assert "total_pages" in body
    assert "data" in body

    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0

    # Validate first user structure
    user = body["data"][0]

    assert "id" in user
    assert "email" in user
    assert "first_name" in user
    assert "last_name" in user
    assert "avatar" in user


def test_create_user_success():
    """
    AT-10
    POST create user successfully
    """

    payload = {
        "name": "Vaibhav",
        "job": "QA Engineer"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload,
        headers=HEADERS,
        timeout=10
    )

    # Status code assertion
    assert response.status_code == 201

    body = response.json()

    # Response body shape assertions
    assert isinstance(body, dict)

    assert "name" in body
    assert "job" in body
    assert "id" in body
    assert "createdAt" in body

    assert body["name"] == "Vaibhav"
    assert body["job"] == "QA Engineer"


def test_login_missing_password():
    """
    AT-11
    POST login request with missing password
    """

    payload = {
        "email": "eve.holt@reqres.in"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=payload,
        headers=HEADERS,
        timeout=10
    )

    # Status code assertion
    assert response.status_code == 400

    body = response.json()

    # Response body shape assertions
    assert isinstance(body, dict)
    assert "error" in body
    assert isinstance(body["error"], str)
    assert len(body["error"]) > 0


def test_get_nonexistent_user():
    """
    AT-12
    GET request for non-existent user
    """

    response = requests.get(
        f"{BASE_URL}/users/999999",
        headers=HEADERS,
        timeout=10
    )

    # Status code assertion
    assert response.status_code == 404

    body = response.json()

    # Response body shape assertion
    assert isinstance(body, dict)

    # Current ReqRes response for this endpoint
    assert body == {}