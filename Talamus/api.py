import requests
import json
from requests.exceptions import HTTPError
from requests.exceptions import Timeout     

url = 'http://localhost:5000/api/'

def request(method, json):
    resp_url = url + method
    try:
        response = requests.post(
            resp_url,
            json=json
        )

        # если ответ успешен, исключения задействованы не будут
        print("Status ", response.status_code)
        print("Text ", response.text)
        print("json ", response.request.body)
        return response.text
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Timeout:
        print('The request timed out')
    except Exception as err:
        print(f'Other error occurred: {err}')

class Auth:
    def __init__(self):
        print("Init Auth class")

    def register(self, data):
        output_json = json.dumps(request("auth/register", data))
        return output_json
    
    def login(self, data):
        output_json = json.dumps(request("auth/login", data))
        return output_json
    
    

class User:
    global token
    token = ""
    def __init__(self, Token):
        global token
        print("Init User class")
        token = str(Token)
    
    def self_profile():
        global token
        output_json = json.dumps(request("user", json = { 'token': token}))
        return output_json