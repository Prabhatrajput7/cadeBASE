import requests, json
# i have changed the urls in project url
def client():
    """case one"""
    credentials = {"username": "udemy", "password": "udemy"}
    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",data=credentials)
    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)
    

    """CAse Two"""
    # token_h = "Token 5b674b3655bdbfd7d3af89efc195fbeed1b938b7"
    # headers = {"Authorization": token_h}
    # response = requests.get("http://127.0.0.1:8000/profiles/",headers=headers)    
    # print("Status Code: ", response.status_code)
    # response_data = response.json()
    # print(response_data)
    """
    Status Code:  200
[{'id': 1, 'user': 'udemy', 'avatar': 'http://127.0.0.1:8000/media/1655898.webp', 'bio': 'Anime', 'city': 'Japan'}, {'id': 3, 'user': 'Ash', 'avatar': 'http://127.0.0.1:8000/media/ash.PNG', 'bio': 'Rusher', 'city': 'Moscow'}, {'id': 4, 'user': 'ela', 'avatar': 'http://   127.0.0.1:8000/media/stylegan-asuka-face-sample_rVsmXGy.webp', 'bio': 'sticking it', 'city': 'poland'}]
    """


    # response = requests.post("http://127.0.0.1:8000/api-token-auth/",data=credentials)



if __name__ == "__main__":
    client()