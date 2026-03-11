import httpx

login_payload = {
    "email": "dmishenko@example.com",
    "password": "user"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status code:", login_response.status_code)

users_me_headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}

users_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=users_me_headers)
users_me_response_data = users_me_response.json()

print("Users me response:", users_me_response_data)
print("Status code:", users_me_response.status_code)
