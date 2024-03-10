# Burda coldeki kvadrat moterize evezine yumru moterizede istifade de etmek olar.
# Yeni, tuple icinde tuple. 
telebeler = (
    ("Cavidan", "F", 60),
    ("Anar", "A", 33),
)


# eyni kodun sorted() funksiyasi ile yazilmasi.

yash = lambda yashlar: yashlar[2]
yahsa_gore_siralama = sorted(telebeler, key=yash)

for i in yahsa_gore_siralama:
    print(i)