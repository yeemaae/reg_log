''''DAY:ZERO console app for registraion & login'''
import registration
import login
import json


def main(data):
    action = input("Welcome to console app! What u want to do? registration or login?")
    if action == "0" or action == "registration":
        registration.registration(data)
    elif action == "1" or action == 'login':
        login.login(data)
    else:
        print("invalid action!")


if __name__ == '__main__':
    while True:
        try:
            with open('data-base.json') as f:
                data = json.load(f)
            main(data)
        except FileNotFoundError:
            data = {
                "users": []
            }
            with open('data-base.json', 'w') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
