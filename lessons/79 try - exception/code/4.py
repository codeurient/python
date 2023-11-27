# Exception - kodunu silersek ve number-i string-e bolersek ne baw verecekdir ?



try:
    bolunen  = int(input("Bir eded daxil edin"))
    bolen = int(input("Bir eded daxil edin"))
    netice = bolunen / bolen
except ZeroDivisionError:
    print("Sifira bolmek olmaz")