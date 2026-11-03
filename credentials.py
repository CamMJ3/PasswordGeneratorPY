import json, os

credentials = []


def get_credentials():
    if not os.path.exists("credentials.json"):
        return []

    with open("credentials.json", "r") as file:
        return json.load(file)


def new_credential(credentials, website, username, password):
    credential = {"website": website, "username": username, "password": password}

    credentials.append(credential)
    save_credential(credentials)


def save_credential(credentials):
    with open("credentials.json", "w") as file:
        json.dump(credentials, file, indent=4)
