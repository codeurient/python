# list icinde olan tuple-i nece siraliya bilerik ?

# ada gore, dereceye gore, yawa gore siralama.

telebeler = [
    ("Cavidan", "F", 60),
    ("Anar", "A", 33),
    ("Seymur", "D", 36),
    ("Huseyn", "B", 20),
    ("Nurlan", "C", 78),
]

# sort() metodu ile siralama edek. 
telebeler.sort()

for i in telebeler:
# ekrana yazdirdiqda tuple-larin 1ci deyerine gore siralanma bas verir. 
# 1ci deyer adlardir. 
    print(i)