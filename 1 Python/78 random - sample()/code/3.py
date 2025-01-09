# sample() funksiyasi eger 3 deyeri olan list olarsa her defe random formada hemin
# deyerlerin yerini deyiserek geri qaytaracaqdir.


import random

ededler = [1, 2, 3]

random_numune = random.sample(ededler, 3)

print(random_numune)