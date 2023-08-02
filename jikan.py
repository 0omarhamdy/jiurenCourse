from time import sleep
from random import randint, choice
from helper_functions import even_or_odd, ftoc, print_sleep, calculator, encrypt, decrypt

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
    print_sleep('Alan Turing!')
    print_sleep("let's encrypt")
    names = ["Omar", "Shahd", "Asmaa","Sarah", "Alaa", "Ammar", "Mariam", "Gehad", "Mohamed", "Dalia", "Aya", "Yousef", "Abdo", "Ali"]
    name = choice(names)
    print_sleep(name)
    enc = encrypt(name)
    print_sleep("it becomes: {enc}")
    print_sleep("now decrypt it!")
    dec = decrypt(enc)
    print_sleep(dec)
    
elif 1870 >= year >= 1840:
    print_sleep('Charles Babbage!')
    print_sleep('Solve the math challenge!')
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    ops = ["+", "-", "*", "/", "**", "%"]
    op = choice(ops)
    print_sleep(f"{num1} {op} {num2} = {calculator(num1, op, num2)}")

else:
    print('Wrong range')
