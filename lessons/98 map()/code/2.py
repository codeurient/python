# 1. kvadrat() adinda oz funksiyamizi yaradiriq ve bu funksiyanin isi "x" parametrinin qebul etdiyi 
# deyerlerin kvadratini qaytarmaqdir.
def kvadrat(eded):
    return eded ** 2

# list yaradiriq
ededler = [1, 2, 3, 4, 5]

# map() metodu list-in icindeki deyerleri avtomatik olaraq bir-bir kvadrat funksiyasinin "x" adli parametrine 
# gonderir. Hemin funksia ise bu deyerlerin kvadratini return edir.
ededlerin_kvadratlari = map(kvadrat, ededler)

# return olan deyerler "ededlerin_kvadratlari" adli variable-nin icinde yaddawa yazilir ve bu deyerleri,
# list() metodu ile yeniden siyahiya cevirerek ekrana yazdiririq.

print(   list(ededlerin_kvadratlari)   )

#! tuple-a yaxud set-e de cevirmek mumkundur.
# print(   tuple(ededlerin_kvadratlari)   )
# print(   set(ededlerin_kvadratlari)   )
