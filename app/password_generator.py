import random
import string

class InputTooSmallError(Exception):
    """ """
    pass

def password_engine(pass_len:int):
    """
    Generate password based on length of characters
    Parameters
    ----------
    pass_len:int : length of password characters
        

    Returns
    -------
    str: Password
    """
    # Sources of data
    letters = string.ascii_letters
    numbers = string.digits
    symbols = '!#$&<=>?@_'

    # Combile into one string
    letters_numbers = letters + numbers + symbols
    
    if pass_len < 10:
        raise InputTooSmallError('Password length should be greater than 9')

    if not isinstance(pass_len, int):
       raise TypeError('Password should not be a decimal')

    password = random.choices(letters_numbers, k=pass_len)

    return ''.join(password)