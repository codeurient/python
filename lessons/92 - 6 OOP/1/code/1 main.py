# Klas metodlarinin zencirvari yazilmasi.

class Masin:

    def xoda_salmaq(self):
        print("Siz motoru xoda saldiniz")

    def surmek(self):
        print("Siz masini surursuz")

    def masini_saxlamaq(self):
        print("Siz masini saxladiniz")

    def masini_sondurmek(self):
        print("Siz masini sondurdunuz")

# klasin obyektini yaradiriq
masin = Masin()

# Stringleri ekrana yazdirmaq ucun once klasin adini yaziriq sonra ise metodun adini.
masin.xoda_salmaq()
masin.surmek()
masin.masini_saxlamaq()
masin.masini_sondurmek()