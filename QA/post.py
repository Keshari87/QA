import requests
import json


#base url
base_url="https://reqres.in/api"

#auth token

auth_token="token...token value"

#post request

def post_request():
    url=base_url+ "/users"
    print("post url: ",url)
    headers={"authorization":auth_token}
    data={
        "name":"manu",
        "email":"manub@gmail.com",
        "job": "QA"

    }
    response = requests.post(url,json=data, headers=headers)
    json_data=response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json post response data", json_str)
    user_id= json_data["id"]
    print("user id= ",user_id)
    assert response.status_code==201

    return user_id

post_request()

