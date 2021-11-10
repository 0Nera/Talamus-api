from Talamus import api
import json

auth = api.Auth()

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
User = api.User(Token="h2xa2Nzz")

Profile = api.User.self_profile()

print(Profile)

ProfileData = json.loads(Profile)
ProfileData = json.loads(ProfileData)

print(type(ProfileData))
print(json.loads(ProfileData['Data']))