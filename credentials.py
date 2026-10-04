import json
credentials = []

def new_credential(website, username, password):
    credential = {"website": website,
                  "username": username,
                  "password": password
    }

    credentials.append(credential)

def save_credential():
    with open("credentials.json", "w") as file:
        json.dump(credentials, file, indent=4)