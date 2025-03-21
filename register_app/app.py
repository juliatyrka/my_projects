import sys
from functions import *
from register_app import functions


#Create a user validation function

def validate_user(name, email, password):
    if functions.validate_name(name) == False:
        raise ValueError('name must be greater than 2 chatacters')

    if functions.validate_email(email) == False:
        raise ValueError('email adress must be valid')

    if functions.validate_password(password) == False:
        raise ValueError('password is too weak')

    return True


def register_user(name,email,password):
    try:
        validate_user(name, email, password)
    except:
        return False


    user_details = {}
    user_details['name'] = name
    user_details['email'] = email
    user_details['password'] = password
    return user_details

register_user('Julia', 'julia@mail.com', 'myPassword123')


