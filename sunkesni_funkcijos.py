# 1.	Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas konsolėje pridedant “---” pradžioje ir gale. PVZ (---labas---)
print("--------1--------")
from random_text_function import generate_rnd_str

rnd_text = generate_rnd_str(75)
print("Random text:",rnd_text)

def hard_one(txt):
    print(f"---{txt}---")

hard_one(rnd_text)

# 2.	Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių). Atspausdinkite simbolius stulpeliu. Jei tai skaičius apgaubkite “ [ 7 ]”. Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75].
print("--------2--------")

def print_symbols(txt):
    number_buffer = ""   # stores consecutive digits

    for ch in txt:
        if ch.isdigit():
            # build a row of numbers
            number_buffer += ch
        else:
            # if we have collected numbers, print them first
            if number_buffer != "":
                print(f"[{number_buffer}]")
                number_buffer = ""

            # print the non-number symbol
            print(ch)

    # print leftover numbers at the end
    if number_buffer != "":
        print(f"[{number_buffer}]")

print_symbols(rnd_text)