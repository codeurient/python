# sample() funksiyası 2 parametr qebul edir. 1ci parametr deyerler olan listdir
# 2ci parametr hemin list-in icinden random formata secilen deyerlerin sayi. 


import random

 
ededler = [1, 2, 3, 4, 5, 6, 7, 8, 9]

random_numune = random.sample(ededler, 3)

print(random_numune)