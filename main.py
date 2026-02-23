import datetime

def say_hi(name):
    print(f"hi {name}")

say_hi("Kosmosas")

def make_initials(txt):
    pts = txt.split()
    res = ""
    print(pts)
    for pt in pts:
        res += pt[0]
    return res.upper()

print(make_initials("Vytautas Dydidis Gediminaitis"))

import datetime
from random import randint
# from funkcijos import is_failo,is_failo_kita
#
# is_failo()

randint(1,5)

def say_hi():#nieko nepriima, nieko negrazina
    print("hi")

say_hi()
say_hi()
say_hi()
for i in range(5):
    say_hi()

def say_hi_to(name):#priima kintamaji, nieko negrazina
    print(f'hi {name}')
    print(":)")

say_hi_to("Jonas")
say_hi_to("Jokubas")
vardas = "Janina"
say_hi_to(vardas)

def sim_pi():#nieko nepriima, grazina reiksme
    return 3.1415

res = sim_pi()
print(res)
print(sim_pi())

def sumavimas(a,b):#priima du kintamuosius, grazina reiksme
    return a + b

res = sumavimas(14,40)
print(res)
print(sumavimas(4,res))

say_hi()

def make_initials(name,surname):
    return (name[0] + surname[0]).upper()

initials = make_initials('naglis',"Mockevicius")
print(initials)

def make_initials_v2(txt):
    pts = txt.split()
    res = ""
    for pt in pts:
        res += pt[0]
    return res.upper()

print(make_initials_v2("Nalglis Jonas Mockevicius"))


def calc_age(birth_year = 0):
    return datetime.date.today().year - birth_year

print(calc_age(1990))
print(calc_age())

range(10)
range(0,10)

def print_info(name = "",surname = "",birth_year = 0):
    print(f'Vartotojas yra {name} {surname}. {calc_age(birth_year)} metu amžiaus. ')

print_info("Naglis",'Mockevicius',1990)
print_info('naglis',1990)
print_info(name='naglis',birth_year=1990)
# print(sep="", end=" ")
print("labas va\nkaras")

#darbas per kelis failus, gal importai

