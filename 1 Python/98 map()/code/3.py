ededler = [1, 2, 3, 4, 5]

# Kodu daha qisa yazmaq ucun lambda funksiyadan da istifade etmek mumkundur.
ededlerin_kvadratlari = map(lambda x: x ** 2, ededler)
# ededler list-indeki deyerler bir-bir lamda funksiyanin x parametrine oturulur

print(   list(ededlerin_kvadratlari)   )



