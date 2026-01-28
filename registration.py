import json
import re


def username_valid():
    attempt = 0
    while True:
        username_pattern = r"^[a-zA-Z0-9._-]{4,20}$"
        username = input("please enter username: ")
        if not re.fullmatch(username_pattern, username):
            attempt += 1
            print(''' Username Invalid,
        - At least 4 characters long, maximum 20.
        - Can contain letters (a-z, A-Z), numbers (0-9), dots (.), underscores (_), and hyphens (-).''')
        else:
            return username
        if attempt == 3:
            return None


def firstname_valid():
    attempt = 0
    while True:
        name_pattern = r"^[A-Za-z]*$"
        firstname = input("please enter firstname: ")
        if not re.fullmatch(name_pattern, firstname):
            attempt += 1
            print("Firstname Invalid: only letters (A–Z, a–z) are allowed. No numbers or symbols.")
        else:
            return firstname
        if attempt == 3:
            return None


def lastname_valid():
    attempt = 0
    while True:
        name_pattern = r"^[A-Za-z]*$"
        lastname = input("please enter lastname: ")
        if not re.fullmatch(name_pattern, lastname):
            attempt += 1
            print("Lastname Invalid: only letters (A–Z, a–z) are allowed. No numbers or symbols.")
        else:
            return lastname
        if attempt == 3:
            return None


def email_valid():
    attempt = 0
    while True:
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        email = input("please enter email: ")
        if not re.fullmatch(email_pattern, email):
            attempt += 1
            print(
                "Email Invalid:\n"
                "- Must be in a valid email format (example: user@example.com).\n"
                "- Local part may contain letters, numbers, and . _ % + -\n"
                "- Domain may contain letters, numbers, dots (.) and hyphens (-).\n"
                "- Top-level domain must contain at least 2 letters."
            )
        else:
            return email
        if attempt == 3:
            return None


def pass_valid():
    attempt = 0
    while True:
        pass_pattern = r'[A-Za-z0-9@#$%^&+=]{8,}'
        password = input("please enter password: ")
        if not re.fullmatch(pass_pattern, password):
            attempt += 1
            print(
                "Password Invalid:\n"
                "- Must be at least 8 characters long.\n"
                "- Allowed characters: letters (A–Z, a–z), numbers (0–9), and symbols @ # $ % ^ & + =.\n"
                "- Spaces and other special characters are not allowed."
            )
        else:
            return password
        if attempt == 3:
            return None


def registration(data):
    att = "You are giving not correct data more than 3 times!!!"
    username = username_valid()
    if username == None:
        print(att)
        return
    firstname = firstname_valid()
    if firstname == None:
        print(att)
        return
    lastname = lastname_valid()
    if lastname == None:
        print(att)
        return
    email = email_valid()
    if email == None:
        print(att)
        return
    password = pass_valid()
    if password == None:
        print(att)
        return

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
