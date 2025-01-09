# Eger movcud mezmunu deyismeden yenisini elave etmek isteyirikse onda mod olaraq "a" demeliyik

# append yeni elave et.

metn = "\n lala and lolo"

with open('example.txt', "a") as sened:
    sened.write(metn)