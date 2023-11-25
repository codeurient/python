# GLOBAL deyiskenleri funksiya icinde istifade etmek ucun global acar sozunden istifade edilir.

# Ancaq meslehet deyildir bele etmek.

ad = "Ali" # GLOBAL variable

def cari_funksiya():
    global ad # GLOBAL variable
    print(ad)
cari_funksiya()

print(ad)