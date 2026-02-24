# from main import make_initials
# make_initials()
# Sukurkite Funkciją kuri priima du kintamuosius, skaičius. Juos susumuoja ir atspausdina.
import random

print("--------1--------")
def sudetis(a,b):
    return a + b

print(sudetis(1,2))

# Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.

print("--------2--------")
def PISq():
    return 9.8596

print(PISq())

# Sukurkite Funkciją kuri priima du kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.
print("--------3--------")
def sandauga(a,b):
    return a * b

print( sandauga(1,2))

# Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina visus elementus vienoje eilutėje.
print("--------4--------")

letters = ["A", "B", "C", "D"]
#
# for i in range(len(letters)):
#     print(letters[i], end=" ")
#
def all_elements(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

all_elements(letters)

# Sukurkite Funkciją kuri sugeneruotų random skaičių masyvą ir jį gražintų. Funkcija priima tris kintamuosius, min, max ir length reikšmėms nustatyti.
print("--------5--------")

def rnd_array(min, max, length):
    array = random.sample(range(min, max), length)
    print(array)
    return array
    # print(*array)

rnd_array5 = rnd_array(1, 10, 5)

# Sukurkite Funkciją kuri panaudotų 5toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.
print("--------6--------")


def rnd_array_sum(array):
    sum6 = 0
    for i in range(len(array)):
            sum6 += array[i]
    return sum6

print(rnd_array_sum(rnd_array5))

# Sukurkite Funkciją kuri priimtų 5toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį.
print("--------7--------")

def rnd_array_avg(array):
    sum7 = 0
    for i in range(len(array)):
            sum7 += array[i]
    return sum7/len(array)

print(rnd_array_avg(rnd_array5))
# print(f"{rnd_array_avg(rnd_array5):.2f}")

# Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis. Pirmas skaičius- išoriniam ciklui, antras vidiniam.

print("--------8--------")

def star_shape(y,x):
    for i in range(y): # vertical
        row = ""
        for j in range(x):  # horizontal
            row += "*"
        print(row)

star_shape(3,4)

# def star_shape(y, x):
#     for i in range(y):
#         print("*" * x)


# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų. Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)
print("--------9--------")

def string_details(txt):
    spaces = 0
    symbols = 0
    for i in txt:
        if i == " ":
            spaces += 1
        else:
            symbols +=1

    print("simbolių yra", symbols)
    print("tarpų yra", spaces)

sakinys = "Šiandien labai graži diena, ane"
string_details(sakinys)

# Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.

print("--------10--------")

def string_coded(txt):
    active_code = ""
    for i in range(len(txt) - 1, -1, -1):
        active_code += txt[i]
    print(active_code)

text_to_code = "Abrahamas Linkolnas"
string_coded(text_to_code)

# Sukurti funkciją, kuri apsuka tik žodžius. “Labas rytas” -> “sabaL satyr” ir atspausdina rezultatą

print("--------11--------")

def reversed_words(txt):
    result = ""
    word = ""
    for i in txt:
        if i != " ":
            word += i
            # print(i)
        else:
            result += word[::-1] + " "
            word = ""
            # print(result)
    # print()
    result += word[::-1]
    print(result)

text_to_code = "United States of America"
reversed_words(text_to_code)

# Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos elementus kurie yra skaičiai.
print("--------12--------")

def only_numbers(array):
    num_array = []
    for i in array:
        if isinstance(i,(int,float)):
            # num_array.append(array[i])
            num_array.append(i)
    print(num_array)

rnd_array12 = [1 ,"2", 3, "4", 5.5]
only_numbers(rnd_array12)


# Sukurkite funkciją, kuri priima masyvą ir atspausdina tik sveikuosius skaičius. (jei pavyks, patobulinkite, kad funkcija priimtų antrą parametrą True/False kuris nuspręstų ar spausdins tik sveikuosius skaičius ar skaičius su kableliu.
print("--------13--------")

def only_int_numbers(array,boolean = True):
    num_array = []
    if boolean == True:
        for i in array:
            if isinstance(i,(int)):
                # num_array.append(array[i])
                num_array.append(i)
        print(num_array)
    else:
        for i in array:
            if isinstance(i,(int,float)):
                num_array.append(i)
        print(num_array)

rnd_array13 = [1 ,"2", 3, "4", 5.5, 7565.4564, 44.44, 654.498, 8, 9, 10, "aaa", "bb"]
only_int_numbers(rnd_array13, False)
only_int_numbers(rnd_array13)

# Sukurkite funkciją word_count kuri priimtų textą ir gražintų kiek jame yra žodžių.
print("--------14--------")

def word_count2(txt):
    words = 0
    check_space = True
    for i in txt:
        if i == " ":
            check_space = True
        else:
            if check_space:
                words += 1
                check_space = False

    print("žodžių yra", words)

sakinys = "Šiandien labai graži diena,  ane tikrai?"
print(sakinys)
word_count2(sakinys)


# Sukurkite funkciją kuri priima du parametrus. Skaičių masyvą ir boolean. Funkcija gražina prafiltruotą masyvą. Kai antras parametras True/tik poriniais skaičiais, False/tik neporiniais skaičiais.
print("--------15--------")

def even_odd(array,boolean = True):
    new_array = []
    if boolean == True:
        for i in array:
            if isinstance(i, (int)):
                if i % 2 == 0:
                    new_array.append(i)
    # print(new_array)
    else:
        for i in array:
            if isinstance(i, (int)):
                if i % 2 != 0:
                    new_array.append(i)
    # print(new_array)

    return new_array

exp_array15 = [1 , 3, 4, 5.5, 7565.4564, 44.44, 654.498, 8, 9, 10]
print("input_array:",*exp_array15)
# array15 = [1 , 3, 4, 8, 9, 10, 11, 12]
# print("input_array:",*array15)

# even_odd(array15, False)

# print(even_odd(array15,))
print(even_odd(exp_array15,))
# print(even_odd(array15,False))
print(even_odd(exp_array15,False))


# Sukurkite funkciją number_is_prime. Funkcija priima skaičių, gražina True/False ar skaičius pirminis.
print("--------16--------")

# rnd_numb_array = random.sample(range(1, 201), 50)
# print(*rnd_numb_array)
# pirminiai = sorted([
#     i for i in numbers9
#     if i > 1 and all(i % d != 0 for d in range(2, int(i**0.5) + 1))
# ])
# print("Pirminiai:", *pirminiai)


rnd_numb = random.randint(1,1000)
print(rnd_numb)

def number_is_prime(number):
    if number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1)):
        return True
    else:
        return False

print(number_is_prime(rnd_numb))




# Sukurkite funkciją kuri priima du argumentus. Gražina pirmąjį skaičių pakeltą laipsniu tokiu kaip antras skaičius.
print("--------17--------")

def exp_degree(a,b):
    return a ** b

print(exp_degree(2,4))


# Sukurkite funkciją kuri priima skaičių masyvą ir gražina tik skirtingus elementus. (panašiai kaip sql distinct)
print("--------18--------")

def rnd_num_array(min, max, length):
    array = []
    for i in range(length):
        array.append(random.randint(min, max))
    return array

array18 = rnd_num_array(0,10,10)
print("input:",*array18)

def unique_array(num_array):
    array_of_unique_values = []

    for i in range(len(num_array)):
        if num_array[i] not in array_of_unique_values:
            array_of_unique_values.append(num_array[i])
    return array_of_unique_values

print(unique_array(array18))

# Sukurkite funkciją kuri priima tekstą ir atspausdina tekste daugiausiai pasikartojantį simbolį.
print("--------19--------")

def generate_rnd_str(length):
  symbols = " ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890 "
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text

rnd_text = generate_rnd_str(50)
print("Text:",rnd_text)

def top_symbol(txt):
    symbol = ""
    counter = 0
    for i in txt:
        count_symbol = txt.count(i)
        if count_symbol > counter:
            counter = count_symbol
            symbol = i

    return symbol

print("Symbol:", top_symbol(rnd_text))

# Sukurkite funkciją kuri priima tekstą ir atspausdina jame esantį ilgiausią žodį.
print("--------20--------")

def top_word(txt):
    txt_to_array = txt.split()
    word = ""

    for i in txt_to_array:
        if len(i) > len(word):
            word = i
    return word

print("Word",top_word(rnd_text), "\nLength", len(top_word(rnd_text)))



