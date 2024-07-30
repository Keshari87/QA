import requests
import json
import random
import string

#base url
base_url="https://reqres.in/api"

#auth token

auth_token="token...token value"

def generate_random_email():
    domain="automation.com"
    email_length=8
    random_string=' '.join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    email=random_string + '@' + domain
    return email
def put_request(user_id):
    url=base_url+ f"/users/{user_id}"
    print("post url: ",url)
    headers={"authorization":auth_token}
    data={
        "name":"manu",
        "email":generate_random_email(),
        "job": "QA"

    }
    response = requests.put(url,json=data, headers=headers)
    json_data=response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json post response data", json_str)

    print("user id= ",user_id)
    assert response.status_code==200
    print("update successfully")
    return user_id

put_request(877)