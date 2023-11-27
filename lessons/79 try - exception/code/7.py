
# Eyni vaxt-da hem oz hemde proqram xeta mesajlarini ekrana yazdirmaq da olar.


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