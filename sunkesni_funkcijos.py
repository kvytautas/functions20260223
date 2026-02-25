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

num = 20
print(num,divisor_count(num))
num = 560
print(num,divisor_count(num))
num = 641
print(num,divisor_count(num))

# 4.	Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 33 iki 77. Išrūšiuokite masyvą pagal daliklių be liekanos kiekį mažėjimo tvarka, panaudodami trečio uždavinio funkciją.
print("--------4--------")

from random_text_function import rnd_num_array

rnd_array = rnd_num_array(33,77,100)
# rnd_array.sort(reverse=False,key=divisor_count)
# print("array:", rnd_array)

def sort_by_divisor_count(array):
    new_array = sorted(array, reverse=True,key=divisor_count)
    return new_array

print("Input:", rnd_array)
print("Output:", sort_by_divisor_count(rnd_array))

# 5.	Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 333 iki 777. Naudodami 3 uždavinio funkciją iš masyvo suskaičiuokite kiek yra pirminių skaičių.
print("--------5--------")

rnd_array = rnd_num_array(333,777,100)

def prime_number_count(array):
    counter = 0
    for i in range(len(array)):
        if divisor_count(array[i]) == 0:
            counter += 1

    return counter

print("Input:", rnd_array)
print("Output:", prime_number_count(rnd_array))

# 6.	Sugeneruokite atsitiktinio (nuo 10 iki 20) ilgio masyvą, kurio visi, išskyrus paskutinį, elementai yra atsitiktiniai skaičiai nuo 0 iki 10, o paskutinis elementas masyvas, kuris generuojamas pagal tokią pat salygą kaip ir pirmasis masyvas. Viską pakartokite atsitiktinį nuo 10 iki 30  kiekį kartų. Paskutinio masyvo paskutinis elementas yra lygus 0;
print("--------6--------")


def array_recursion(input):
    if input == 0:
        return 0

    rnd_array_len = random.randint(10, 20)

    array = [random.randint(0, 10) for i in range(rnd_array_len)]

    array[-1] = array_recursion(input - 1)

    return array

input = random.randint(1, 3)
result_array = array_recursion(input)

print(input)
print(result_array)

# 7.	Suskaičiuokite šešto uždavinio elementų, kurie nėra masyvai, sumą. Skaičiuoti reikia visuose masyvuose ir submasyvuose.
print("--------7--------")

def array_nested_sum(array):
    total = 0

    for element in array:
        if isinstance(element, list):
            total += array_nested_sum(element)  # if the element is a list, sum it recursively
        else:
            total += element             # if it's a number, add it directly

    return total

print("input array:",result_array)
print("sum",array_nested_sum(result_array))

# 8.	Sugeneruokite masyvą iš trijų elementų, kurie yra atsitiktiniai skaičiai nuo 1 iki 33. Jeigu tarp trijų paskutinių elementų yra nors vienas ne pirminis skaičius, prie masyvo pridėkite dar vieną elementą- atsitiktinį skaičių nuo 1 iki 33. Vėl patikrinkite pradinę sąlygą ir jeigu reikia pridėkite dar vieną elementą. Kartokite, kol sąlyga nereikalaus pridėti elemento.
print("--------8--------")

def number_is_prime(number):
    if number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1)):
        return True
    else:
        return False
def rnd_num_array(min, max, length):
  array = []
  for i in range(length):
    array.append(random.randint(min, max))
  return array

rnd_arr = rnd_num_array(1,33,3)
print(rnd_arr)
# random_array = random.sample(range(1, 33), 3) # random unique
# print(random_array)

print(number_is_prime(rnd_arr[0]),number_is_prime(rnd_arr[1]),number_is_prime(rnd_arr[2]))

def array_of_primes(array):

    while True:
        new_array = array[-3:]
        if len(new_array) == 3 and all(number_is_prime(i) for i in new_array):
            return array

        rnd_num = random.randint(1,33)
        array.append(rnd_num)

print(array_of_primes(rnd_arr))


# 9.	Sugeneruokite masyvą iš 10 elementų, kurie yra masyvai iš 10 elementų, kurie yra atsitiktiniai skaičiai nuo 1 iki 100. Jeigu tokio didelio masyvo (ne atskirai mažesnių) pirminių skaičių vidurkis mažesnis už 70, suraskite masyve mažiausią skaičių (nebūtinai pirminį) ir prie jo pridėkite 3. Vėl paskaičiuokite masyvo pirminių skaičių vidurkį ir jeigu mažesnis nei 70 viską kartokite.
print("--------9--------")

massive_array = []
for i in range(10):
    random_array = (rnd_num_array(1,100,10))
    massive_array.append(random_array)

print(massive_array)

total = 0
massive_array_sums = []
for array in massive_array:
    massive_array_sums.append(sum(array))

print(massive_array_sums)