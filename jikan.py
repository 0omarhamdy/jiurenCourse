from time import sleep
from random import randint
from helper_functions import even_or_odd, ftoc, print_sleep

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
    print_sleep("let's go for the next Level!")
    num = randint(0, 10000)
    print_sleep(even_or_odd(num))

elif  1950 >= year >= 1930:
    print('Alan Turing!')
    
elif 1870 >= year >= 1840:
    print('Charles Babbage!')

else:
    print('Wrong range')
