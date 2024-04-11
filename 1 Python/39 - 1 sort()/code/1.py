# sort() metodu deyerleri elifbasi sirasina gore nizamliyir.

# sort() metodu movcud siyahini deyisdirir yeni list qaytarmir

# Bundan ferqli olaraq sorted() funksiyasi vardir hansiki movcud olani yox
# yeni siyahi yaradir ve movcud siyahi oldugu kimi qalir. (diger ders)

telebeler = ["Cavidan", "Anar", "Seymur", "Huseyn", "Nurlan"]


telebeler.sort()

for i in telebeler:
    print(i)

print(telebeler)