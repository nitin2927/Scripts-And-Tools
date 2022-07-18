# Strong passsword generator

import sys
import random
import string
from passwordmeter import test


def generate_password(length):
    symbol = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for i in range(length):
        password += random.choice(symbol)
    return password

# Checking if the password is strong


def check_password(length):

    new_password = generate_password(length)
    score = 0.0
    description = ''
    while score < 0.8:
        new_password = generate_password(length)
        score, description = test(new_password)
    return new_password, score, description


if __name__ == '__main__':
    len = int(sys.argv[1])
    result = check_password(len)
    print("Here is a strong password: " + result[0])
    print("Password score: " + str(result[1]))
    print("Password description: ")
    print(result[2])
