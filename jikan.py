from time import sleep
from random import randint


def ftoc(f):
    c = (f - 32) / 1.8
    return c


def print_sleep(text, time=0.5):
    print(text)
    sleep(time)


print_sleep('Welcome to Jikan')

name = input('name: ')
hour = int(input('hour: '))
minute = int(input('minute: '))
id = hour * minute

print_sleep(f"welcome dear {name}, your id = {id}")

year = int(input('which year you want to jump into: '))


print_sleep(f'you jumped to {year}')
print('and met', end=' ')
sleep(0.5)

if 2023 > year >= 1995:
    print_sleep('Demis Hassabis!')
    print_sleep("D: Hi")
                
    f = randint(40, 90)
    print_sleep(f"D: it's {f} f")
    print_sleep("D: Ready to solve London Temp challenge")
    ready = input('ready to ?')
    print_sleep("let's excute your ftoc function!")
    
    c = ftoc(f)
    print_sleep(f"{f} is {c: .1f} C")
    print_sleep("Awesome!")

elif  1950 >= year >= 1930:
    print('Alan Turing!')
    
elif 1870 >= year >= 1840:
    print('Charles Babbage!')

else:
    print('Wrong range')