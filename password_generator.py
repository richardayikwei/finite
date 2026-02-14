import random
import string


def password_generator():
    # Sources of data
    letters = string.ascii_letters
    numbers = string.digits
    symbols = '!#$&<=>?@_'

    # Combile into one string
    letters_numbers = letters + numbers + symbols

    password = random.choices(letters_numbers, k=10)

    return ''.join(password)

if __name__ == '__main__':
    print(password_generator())

