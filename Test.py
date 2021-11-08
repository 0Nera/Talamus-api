from Talamus import api
import json

Handle = api.User()

"""Handle.register(
    data={
            "email": "SynapseOS@gmail.com",
            "password": "SynapseOS_Forever"
        }
    )

Handle.login(
    data={
            "email": "SynapseOS@gmail.com",
            "password": "SynapseOS_Forever"
        }
    )"""

Profile = Handle.self_profile(
    token="FYIorHyq"
    )

Profile = json.loads(Profile)
print(Profile)
print(type(Profile['Data']))
print(
    json.loads(
        Profile['Data']
        )
        )
print(type(Profile))