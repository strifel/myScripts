import requests
import json

print("Welcome to archiver.")
token = input("Please paste a access token: ")
print("Thanks.")
while True:
    repo = input("Input the repo url: ").replace("github.com/", "api.github.com/repos/")
    anwser = requests.patch(repo, data=json.dumps({"archived": True}), headers={"Authorization": "Bearer " + token})
    print(anwser)
