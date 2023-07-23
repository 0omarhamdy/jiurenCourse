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