class Masin:

    def xoda_salmaq(self):
        print("Siz motoru xoda saldiniz")

    def surmek(self):
        print("Siz masini surursuz")

    def masini_saxlamaq(self):
        print("Siz masini saxladiniz")

    def masini_sondurmek(self):
        print("Siz masini sondurdunuz")

masin = Masin()

# Eger metodu zencirvari yazsaq xeta mesaji alariq. xoda_salmaq() metodunun deyerini 
# goreciyik ancaq surmek() metodu xeta verecek cunki zencirvari qayda dogru formada yazilmayib
masin.xoda_salmaq().surmek()