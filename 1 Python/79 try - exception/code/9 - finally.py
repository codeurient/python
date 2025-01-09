# 1. finally - kod ister xeta versin ister xeta vermesin, yenede en sonda, finalda nese 
# ekrana yazdirmaq isteyirikse, yaxud her hansisa bir kodu iwe salmaq isteyirikse finally kod 
# blokundan istifade edirik. 

try:
    bolunen  = int(input("Bir eded daxil edin"))
    bolen = int(input("Bir eded daxil edin"))
    netice = bolunen / bolen
except ZeroDivisionError as e:
    print(e)
    print("Sifira bolmek olmaz")
except ValueError as e:
    print(e)
    print("String-e bolmek olmaz")
except Exception as e:
    print(e)
    print("Bir xeta var")
else:
    print(netice)
finally: 
    print("Bura her zaman iwleyecek hissedir.")