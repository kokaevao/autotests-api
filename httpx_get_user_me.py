import httpx

login_payload = {
  "email": "alex123@test.ru",
  "password": "1234"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Status Code v1/authentication/login:", login_response.status_code)
print("login_response:", login_response_data)


client = httpx.Client(headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"})
me_response = client.get("http://localhost:8000/api/v1/users/me")
print("Status Code v1/users/me:", me_response.status_code)
print("Me_response:", me_response.json())
