import json

with open('data-base.json') as f:
    data = json.load(f)


def registration():
    username = input("please enter username: ")
    firstname = input("please enter firstname: ")
    lastname = input("please enter lastname: ")
    email = input("please enter email: ")
    password = hash(input("please enter password: "))
    repassword = hash(input("please confirm the password: "))

    newuser = dict(username=username,
                   profile=dict(firstName=firstname,
                                lastName=lastname,
                                email=email))
    if password == repassword:
        newuser['password'] = str(password)
    else:
        print("Your password Not match! pls try again!")
        return

    for user in data['users']:
        if user['username'] == username:
            print("This username already in use! Try to login!")
            return

    data['users'].append(newuser)
    with open('data-base.json', 'w') as f:
        json.dump(data, f)
