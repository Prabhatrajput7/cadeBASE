import requests

def client():
    """Case One"""
    data = {
        "username": "resttest2", 
        "email": "test@rest2.com",
        "password1": "changeme123",
        "password2": "changeme123"
        }
    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",data=data)
    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()