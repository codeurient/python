class Masin:
    def xoda_salmaq(self):
        print("Siz motoru xoda saldiniz")
        return self

    def surmek(self):
        print("Siz masini surursuz")
        return self

    def masini_saxlamaq(self):
        print("Siz masini saxladiniz")
        return self

    def masini_sondurmek(self):
        print("Siz masini sondurdunuz")
        return self

masin = Masin()

# metodlar eger cox olarsa onlari yan-yana yazaraq uzatmaq oxumani cetinlesdireceyi ucun, hemin 
# metodlari alt-alta yazmaq mumkundur. Sadece her metodun onune ters slesh yazmaq lazimdir.
masin.xoda_salmaq()\
     .surmek()\
     .masini_saxlamaq()\
     .masini_sondurmek()