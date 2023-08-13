from random import randint

def vowels(name):
    vs = ('e','a','u','i','o')
    c = 0
    for ch in name:
     if ch in vs:
       c +=1
    return c
    

print(vowels("omar"))
print("###################################################")


def bmi_calculator(m,h):
    return m/(h**2)


def bmi_cat(bmi):
    if bmi < 18.5:
        return "under"
    elif  25 > bmi >= 18.5:
        return "normal"
    elif 40 > bmi >= 25:
        return "over"
    elif bmi >= 40:
        return "obese"


bmi = bmi_calculator(70, 1.75)
cat = bmi_cat(bmi)
print(f"bmi = {bmi}, cat = {cat}")
print("###################################################")


def guess(nt=5):
    tg = randint(0, 100)
    for i in range(nt):
        g = int(input("guess: "))
        if g == tg:
             print("win")
             break
        elif g < tg:
            print("low")
        elif g > tg:
            print("high")
        
    print("true guess =", tg)
        
nt = int(input("tries: "))
guess(nt)
print("###################################################")