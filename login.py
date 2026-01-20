import json

with open('data-base.json') as f:
    data = json.load(f)


def login():
    username = input("please enter username: ")
    password = hash(input("please enter password: "))

    user = None
    for user in data['users']:
        if user['username'] == username:
            user = user
    if user:
        if user['password'] == str(password):
            print(f'Welcome back {username}')
        else:
            print(user['password'])
            print(str(password))
            print('username or password is incorrect!')
    else:
        print('username or password is incorrect!')
