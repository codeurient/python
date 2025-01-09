# deyerleri tersine siralamaq ucun ise reverse=True arqumentinden istifade edilir

# varsayilan deyer reverse=False olaraq qeyd edilmisdir. Yeni yazmasaq bele bu arqumenti o movcuddur.

yemek = ["pizza", "pendir", "dolma", "merci"]

yemek.sort()

for deyerler in yemek:
    print(deyerler)