def login(data):
    username = input("please enter username: ")
    password = hash(input("please enter password: "))

    incorrect = False
    for user in data['users']:
        incorrect = True
        if user['username'] == username:
            if user['password'] == str(password):
                print(f'Welcome back {username}')
                return
            else:
                print('username or password is incorrect!')
                return
    if incorrect:
        print('username or password is incorrect!')
        return
