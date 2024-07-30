import requests
import json


#base url
base_url="https://reqres.in/api"

#auth token

auth_token="token...token value"

def get_request(page):
    url=f"{base_url}/users?id={page}"
    print(f"get url:  +{url}")
    headers={"authorization": auth_token}if auth_token else {}
    response=requests.get(url, headers=headers)
    assert response.status_code ==200
    json_data=response.json()
    json_str=json.dumps(json_data, indent=4)
    print(f"json get response body{page}:",json_str)
    print("....get user is done...")


get_request(4)
