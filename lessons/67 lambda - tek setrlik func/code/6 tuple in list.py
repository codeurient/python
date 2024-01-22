# tuple icindeki deyerler indekslenmis oldugu ucun 
# 1ci deyerin indeksi 0-dir
# 2ci deyerin indeksi 1-dir
# 3ci deyerin indeksi 2-dir
telebeler = [
    ("Cavidan", "F", 60),
    ("Anar", "A", 33),
    ("Seymur", "D", 36),
    ("Huseyn", "B", 20),
    ("Nurlan", "C", 78),
]

# dereceler[1] dedikde "F", "A", "D", "B", "C" bulari nezerde tutmus oluruq.
# Bu deyerleri "derece" adli variable-a gonderirik.
derece = lambda dereceler: dereceler[1]

# sort() metoduna arqument kimi "derece" variable-ini verdikde, hemin bu metod
# deyerleri avtomatik olaraq siralayacaqdir.
telebeler.sort(key=derece)

for i in telebeler:
    print(i)


# Diger numunede buna ehtiyac yox idi cunki sort() metodu avtomatik olaraq 1ci deyerleri
# siralayirdi. Ancaq birden cox deyer olduqda yazaraq bildirmeliyik ki, hansi deyere gore 
# siralama bas versin. 
    
# Fikir verdinizse () yumru moterizeleri yazmadiq. Yumru moterizeni yazsa idik funksiyani 
# cagirmis olacaqdiq. Elave olaraq eger yumru moterize yazsa idik onda arqument de elave
# etmeli idik.