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


def bekh_fekh(n=100):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print("بخ فخ")
        elif i % 3 == 0:
            print("بخ")
        elif i % 5 == 0:
            print("فخ")
        else:
            print(i)

bekh_fekh()
print("###################################################")

def currency_exchanger(cur, amount):
    curs = {'USD': 31, 'EUR': 34, 'GBP': 40, 'JPY':0.2, 'RUB':0.3}
    r = curs[cur] * amount
    return r


print(currency_exchanger('JPY', 10000))
print("###################################################")
