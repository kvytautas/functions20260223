import random

def generate_rnd_str(length):
  symbols = " ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890 "
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text

def rnd_num_array(min, max, length):
  array = []
  for i in range(length):
    array.append(random.randint(min, max))
  return array