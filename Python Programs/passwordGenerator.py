import random

def passGen():
    rand = random.Random()
    for i in range(7):
        letters = rand.choice('abcdefghijklmnopqrstuvwxyz')
        if i == 0:
            password = letters
            password = password.upper()
            continue
        password += letters
        if i == 6:
            password += rand.choice('123456789')
            return password

def passwordsGen():
    for i in range (5):
        print(passGen())

passwordsGen()
