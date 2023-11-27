# Eger oz xeta mesajlarimizi deyilde Proqramin evvelceden teyin etmis oldugu 
# xeta mesajlarini ekrana yazdirmaq isteyirikse onda "as e" ifadesinden istifade ede bilerik.

# Xeta bas verdikde ZeroDivisionError, ValueError veyaxud Exception kodlari hemin xetalari
# e variable-ina gonderecekdir. Hemin xetani print(e) deyerek ekrana yazdira bilerik. 

# Bu xeta mesajlari ingilis dilindedir.

try:
    bolunen  = int(input("Bir eded daxil edin"))
    bolen = int(input("Bir eded daxil edin"))
    netice = bolunen / bolen
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)