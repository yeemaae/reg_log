''''DAY:ZERO console app for registraion & login'''
import registration
import login


def main():
    action = input("Welcome to console app! What u want to do? registration or login?")
    if action == "0" or action == "registration":
        registration.registration()
        print('done reg')
    elif action == "1" or action == 'login':
        login.login()
        print('done log')
    else:
        print("invalid action!")


if __name__ == '__main__':
    while True:
        main()
