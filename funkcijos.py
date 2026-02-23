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

print(f"{rnd_array_avg(rnd_array5):.2f}")

# Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis. Pirmas skaičius- išoriniam ciklui, antras vidiniam.
# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų. Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)
# Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.
# Sukurti funkciją, kuri apsuka tik žodžius. “Labas rytas” -> “sabaL satyr” ir atspausdina rezultatą
# Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos elementus kurie yra skaičiai.
# Sukurkite funkciją, kuri priima masyvą ir atspausdina tik sveikuosius skaičius. (jei pavyks, patobulinkite, kad funkcija priimtų antrą parametrą True/False kuris nuspręstų ar spausdins tik sveikuosius skaičius ar skaičius su kableliu.
# Sukurkite funkciją word_count kuri priimtų textą ir gražintų kiek jame yra žodžių.
# Sukurkite funkciją kuri priima du parametrus. Skaičių masyvą ir boolean. Funkcija gražina prafiltruotą masyvą. Kai antras parametras True/tik poriniais skaičiais, False/tik neporiniais skaičiais.
# Sukurkite funkciją number_is_prime. Funkcija priima skaičių, gražina True/False ar skaičius pirminis.
# Sukurkite funkciją kuri priima du argumentus. Gražina pirmąjį skaičių pakeltą laipsniu tokiu kaip antras skaičius.
# Sukurkite funkciją kuri priima skaičių masyvą ir gražina tik skirtingus elementus. (panašiai kaip sql distinct)
# Sukurkite funkciją kuri priima tekstą ir atspausdina tekste daugiausiai pasikartojantį simbolį.
# Sukurkite funkciją kuri priima tekstą ir atspausdina jame esantį ilgiausią žodį.




# sunkesni
# rnd_str = generate_rnd_str(400)

