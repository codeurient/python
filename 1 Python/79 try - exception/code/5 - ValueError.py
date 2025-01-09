# ValueError - kodu number-i string-e bolmek istedikde eger xeta bas vererse, 
# bu haqqda ekrana xeta mesaji yazdirmaq ucun istifade edilir.



try:
    bolunen  = int(input("Bir eded daxil edin"))
    bolen = int(input("Bir eded daxil edin"))
    netice = bolunen / bolen
except ZeroDivisionError:
    print("Sifira bolmek olmaz")
except ValueError:
    print("String-e bolmek olmaz")