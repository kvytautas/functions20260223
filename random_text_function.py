import random

def generate_rnd_str(length):
  symbols = " ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890 "
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text