import requests
import json
res = requests.get("https://reqres.in/api/users/2")
assert res.status_code == 200
print(res.json())
