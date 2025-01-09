telebeler = [

    ("Cavidan", "F", 60),

    ("Anar", "A", 33),

]


# lambda funksiyani elave variable-a vermeyerek bir basa sort() metodunun icinde de 
# yaza bilerdik.

telebeler.sort(key=lambda dereceler: dereceler[1])

for i in telebeler:
    print(i)