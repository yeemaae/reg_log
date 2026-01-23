import json
import re


def username_valid():
    while True:
        username_pattern = r"^[a-zA-Z0-9._-]{4,20}$"
        username = input("please enter username: ")
        if not re.fullmatch(username_pattern, username):
            print(''' Username Invalid,
        - At least 4 characters long, maximum 20.
        - Can contain letters (a-z, A-Z), numbers (0-9), dots (.), underscores (_), and hyphens (-).
            ''')
        else:
            return username


def firstname_valid():
    while True:
        name_pattern = r"^[A-Za-z]*$"
        firstname = input("please enter firstname: ")
        if not re.fullmatch(name_pattern, firstname):
            print("Invalid Firstname")
        else:
            return firstname


def lastname_valid():
    while True:
        name_pattern = r"^[A-Za-z]*$"
        lastname = input("please enter lastname: ")
        if not re.fullmatch(name_pattern, lastname):
            print("Invalid Lastname")
        else:
            return lastname


def email_valid():
    while True:
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        email = input("please enter email: ")
        if not re.fullmatch(email_pattern, email):
            print("Invalid email")
        else:
            return email


def pass_valid():
    while True:

        pass_pattern = r'[A-Za-z0-9@#$%^&+=]{8,}'
        password = input("please enter password: ")
        if not re.fullmatch(pass_pattern, password):
            print("Invalid password")
        else:
            return password


def registration(data):
    username = username_valid()
    firstname = firstname_valid()
    lastname = lastname_valid()
    email = email_valid()
    password = pass_valid()
    repassword = input("please confirm the password: ")

    newuser = dict(username=username,
                   profile=dict(firstName=firstname,
                                lastName=lastname,
                                email=email))
    if password == repassword:
        newuser['password'] = str(hash(password))
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
    print(f"REGISTRATION DONE {username}")
