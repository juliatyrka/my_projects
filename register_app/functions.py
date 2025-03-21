registered_users = []

def validate_name(name):
    ''' Checks that the name is greater than 2 chatacters
    Args: name(str)'''

    if type(name) != str:
        raise TypeError('name must be a string')
    elif len(name) < 2:
        raise ValueError('name must be greater than 2 chatacters')
    else:
        return True

def validate_email(email):
    ''' Checks that the email is valid
    Args: email(str)'''

    valid_email = False
    username = email.split('@')[0]

    if '@' not in email:
        return valid_email
    if len(username) < 2:
        raise ValueError('username must be greater than 2 chatacters')
    else:
        valid_email = True

    return valid_email

def validate_password(password):
    ''' Checks that the password is valid
    Args: password(str)'''

    has_capital = False
    has_numbers = False

    if len(password) < 8:
        raise ValueError('password must be greater than 8 characters')
    for char in password:
        if 'A' <= char <= 'Z':
            has_capital = True
        if '0' <= char <= '9':
            has_numbers = True
    if has_capital and has_numbers:
        return True
    else:
        return False

