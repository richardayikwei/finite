import random
import string

# Sources of data
letters = string.ascii_letters
numbers = string.digits
symbols = '!#$&<=>?@_'

letters_numbers = letters + numbers + symbols

print(random.choices(letters_numbers, k=10))
print(len(letters_numbers))
