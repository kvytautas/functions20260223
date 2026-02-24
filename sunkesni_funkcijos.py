import random

# 1.	Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas konsolėje pridedant “---” pradžioje ir gale. PVZ (---labas---)
print("--------1--------")
from random_text_function import generate_rnd_str

rnd_text = generate_rnd_str(75)
print("Random text:",rnd_text)

def hard_one(txt):
    print(f"---{txt}---")

hard_one(rnd_text)

# 2.	Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių). Atspausdinkite simbolius stulpeliu. Jei tai skaičius apgaubkite “ [ 7 ]”. Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75].
# print("--------2--------")
#
# def print_symbols(txt):
#     number_check = ""   # skaiciu eile
#
#     for i in txt:
#         if i.isdigit():
#             number_check += i
#         else:
#             if number_check != "":
#                 print(f"[{number_check}]")
#                 number_check = ""
#             print(i)
#     if number_check != "":
#         print(f"[{number_check}]")
#
# print_symbols(rnd_text)

# 3.	 Parašykite funkciją, kuri skaičiuotų, ir gražintų iš kiek sveikų skaičių jos argumentas dalijasi be liekanos (išskyrus vienetą ir patį save). Pvz padavus 10 turi grąžinti 2,  o padavus 20 gražintų 4.
print("--------3--------")

# rnd_num = random.randint(1,1000)
# print(rnd_num)

def divisor_count(number):
    counter = 0
    # if number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1)):
    #     return 0
    for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                counter += 1
                if i != number // i:
                    counter += 1

    return counter

print(divisor_count(20))

# 4.	Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 33 iki 77. Išrūšiuokite masyvą pagal daliklių be liekanos kiekį mažėjimo tvarka, panaudodami trečio uždavinio funkciją.
print("--------4--------")

