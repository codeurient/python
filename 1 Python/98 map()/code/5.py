# list yaradiriq ve list icinde tuple() yaradiriq.
bazar_dollar_ile = [("kofta", 20.00),
                    ("salvar", 25.00),
                    ("jaket", 50.00),
                    ("naski", 10.00)]

# lambda funksiyanin solunda dayanan "data" parametri, hemin yuxarda dayanan tuple deyerlerini avtomatik elde edir.
# data[0] - 1ci deyerlerdir.
# data[1] - 2ci deyerlerdir. 2i ci deyerleri gunun mezennesine vururuq. 
euro_cevir = lambda data: (data[0], data[1] * 0.82)

# map() metodu hemin 2ci deyerleri bir-bir lambda funksiyaya gonderir ki, hemin deyerleri 0.82 ededine vuraq.
# list() metodu ile geri qayidan deyerleri siyahiya cevrerek, yeni deyiskene otururuk.
bazar_euro_ile =  map(euro_cevir, bazar_dollar_ile) 


for i in bazar_euro_ile:
    print(i)
















# euro_cevir = lambda data: (data[0], str((data[1] * 0.82)) + "€")
