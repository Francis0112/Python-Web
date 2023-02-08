

import random
import uuid
import secrets
import string

def bits16(n):
    res = secrets.token_bytes(n)
    return res

def hex32(n):
    res = secrets.token_hex(n) 
    return res

def meth():
    token = "dragon.com/onegai/memengcat/legendary_items/gift_code="
    token+=secrets.token_urlsafe(16)
    return token

def universal_id(n):
    x = uuid.uuid4()
    y = uuid.uuid3(uuid.NAMESPACE_OID, n)
    return y


def generate_password():
    source = string.ascii_letters+string.digits+string.punctuation
    password = secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(string.punctuation)

    for i in range(6):
        password += secrets.choice(source)

    list1 = list(password)
    secrets.SystemRandom().shuffle(list1)
    password = "".join(list1)
    return password

# print(generate_password())
# print(meth())
# print(bits16(16))
# print(hex32(32))
# a = bits16(16)
# b = hex32(32)
# c = hex32(29)
# x = secrets.compare_digest(b,c)
# print(x)
# print(universal_id("francis"))

# Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5
def gen3():
   counter = 0
   while counter<3:
       x = random.randrange(100,999)
       if x%5==0:
           print(x)
           counter+=1
       if counter==3:
           break
# gen3()

# Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
def panalo():
    a = []
    for i in range(100):
        a.append(random.randrange(100))
    res = random.sample(a, 2)
    return res
# print(panalo())

# Exercise 3: Generate 6 digit random secure OTP
def netflix():
    for i in range(6):
        print(secrets.randbelow(10), end=" ")
# netflix()

# Exercise 4: Pick a random character from a given String
def ozark():
    name = "francis"
    return random.choice(name)
# print(ozark())

# Exercise 5: Generate random String of length 5
def idk_what_to_name_functions():
    source = string.ascii_letters
    n = ""
    for i in range(5):
        n+=random.choice(source)
    return n
# print(idk_what_to_name_functions())

# Exercise 6: Generate a random Password which meets the following conditions
def already_did():
    pass
# already_did()

# Exercise 7: Calculate multiplication of two random float numbers
# First random float number must be between 0.1 and 1
# Second random float number must be between 9.5 and 99.5
def mul():
    a = random.uniform(0.1, 1)
    b = random.uniform(9.5, 99.5)
    res = a*b
    return res
# print(mul())

# Exercise 8: Generate random secure token of 64 bytes and random URL
def security_token():
    x = secrets.token_hex(64)
    y = secrets.token_urlsafe(64)
    return x, y
# print(security_token())

# Exercise 9: Roll dice in such a way that every time you get the same number
def dice():
    for i in range(3):
        random.seed(3)
        print(random.randrange(1,6))
# dice()






