import requests
from requests import auth
from requests.auth import HTTPBasicAuth
from django.conf import settings

import keys


def generate_access_token():
    
    
    res = requests.get(keys.ACCESS_TOKEN_URL, auth=HTTPBasicAuth(keys.CONSUMER_KEY, keys.CONSUMER_SECRET))
    
    json_response = res.json()
    
    access_token = json_response["access_token"]
    
    print(access_token)
    
    return access_token

generate_access_token()
