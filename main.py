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

