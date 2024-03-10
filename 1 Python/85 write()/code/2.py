# Eger movcud mezmunu deyismeden yenisini elave etmek isteyirikse onda mod olaraq "a" demeliyik

# append yeni elave et.

metn = "lala and lolo"

with open('test.txt', "a") as sened:
    sened.write(metn)