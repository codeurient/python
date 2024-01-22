def kvadrat(eded):
    return eded ** 2

ededler = [1, 2, 3, 4, 5]

ededlerin_kvadratlari = map(kvadrat, ededler)

# for dongusu ile butun ededleri tek tek ekrana yazdira bilerik
for i in ededlerin_kvadratlari:
    print(i)