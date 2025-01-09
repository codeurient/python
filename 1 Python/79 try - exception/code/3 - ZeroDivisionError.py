# ZeroDivisionError - sifira bolmek olmaz mesajini elde etmek ucundur.

try:
    bolunen  = int(input("Bir eded daxil edin"))
    bolen = int(input("Bir eded daxil edin"))
    netice = bolunen / bolen
except ZeroDivisionError:
    print("Sifira bolmek olmaz")
except Exception:
    print("Bir weyler yanliwdir")