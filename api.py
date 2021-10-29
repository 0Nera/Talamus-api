import requests
import json
from requests.exceptions import HTTPError
from requests.exceptions import Timeout          

url = 'http://localhost:5000/api/auth/login'

try:
    response = requests.post(
        url, 
        json={
            "email": "slizen.can@gmail.com1",
            "password": "f742dd189a4e7cabd0b99990bb03ed310ba482d3"
        }
    )

    # если ответ успешен, исключения задействованы не будут
    print()
    print()
    print("Status ", response.status_code)
    print("Text ", response.text)
    #json_data = response.json
    print("json ", response.request.body)
    print(response.json())
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Timeout:
    print('The request timed out')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')
