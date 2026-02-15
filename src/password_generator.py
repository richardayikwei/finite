import random
import string

class InputTooSmallError(Exception):
    '''Raised when the input value is less than 10'''
    pass

def password_generator(pass_len=10):
    # Sources of data
    letters = string.ascii_letters
    numbers = string.digits
    symbols = '!#$&<=>?@_'

    # Combile into one string
    letters_numbers = letters + numbers + symbols
    
    if pass_len < 10:
        raise InputTooSmallError('Password length should be greater than 9')

    password = random.choices(letters_numbers, k=pass_len)

    return ''.join(password)

