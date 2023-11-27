# her wey qaydasindadirsa onda neticeni ekrana yazdirmaq ucun en sonda else yazaraq bunu ede bilerik.

# else yeni eks halda demekdir.


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