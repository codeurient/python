# Bu cur xetalarin qarwini almaq ucun kodu yoxlamaq lazimdir.

# Kodu avtomatik yoxlayan python kodunun adi try-dir
# Yeni ilk once yazdigimiz kodu "try" metodunun icinde yerlesdiririk.

# try kodu yoxlayir ve eger bir xeta varsa "except" hemin xetani qebul edir.
# Xeta mesaji olaraq ekrana istediyiniz yazini yazdira bilersiz.

# Exception - bu kod umumu xeta mesajlarinin hamisini elde etmek ucundur. 
try:
    bolunen  = int(input("Bir eded daxil edin"))
    bolen = int(input("Bir eded daxil edin"))
    netice = bolunen / bolen
except ZeroDivisionError:
    print("Bir weyler yanliwdir")