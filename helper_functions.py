from time import sleep
from random import randint


def print_sleep(text, time=0.5):
    print(text)
    sleep(time)


def ftoc(f):
    c = (f - 32) / 1.8
    return c


def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    

def encrypt(text, key=4):
    encrypted_text = ""

    for char in text:
        encrypted_text += chr(ord(char) + key)

    return encrypted_text


def decrypt(text, key=4):
    decrypted_text = ""
    
    for char in text:
        decrypted_text += chr(ord(char) - key)

    return decrypted_text


def calculator(num1, op, num2):
    return eval(f"{num1} {op} {num2}")
    # use conventioal if to make the calc if you want

