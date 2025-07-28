# sorted() funksiyasi ise tipinden asili olmadan hem list ile hem de tuple 
# ile isleyir ve movcud olani yox yeni siyahi yaradir ve movcud siyahi
# oldugu kimi qalir. 

# telebeler.sort()
# Yeni bele yazmaq olmadigi ucun mecbur yeni variable yaradib yazmaliyiq.

# telebeler = ["Cavidan", "Anar", "Seymur", "Huseyn", "Nurlan"] - tuple
# telebeler = ("Cavidan", "Anar", "Seymur", "Huseyn", "Nurlan") - list

telebeler = ["Cavidan", "Anar", "Seymur", "Huseyn", "Nurlan"]

yeni_siralama = sorted(telebeler)

for i in yeni_siralama:
    print(i)





# sort() - metod - cunki kankret bir tip olan list ile isleyir
# sorted() - funksiya - ferqi yoxdu list, tuple. 
