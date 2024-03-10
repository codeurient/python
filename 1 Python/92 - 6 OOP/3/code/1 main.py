class Masin:
# Zencirvari yazilis qaydasinin islemesi ucun her metod return ederek ozunu 
# qaytarmalidir. Yeni, zencirvari metod yazilisinin islemesi ucun olan qayda 
# her bir metodun ozunu return etmesidir.
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

# Metodlarin yerlerinin sira ile yazilmasi vacib deyildir. Yeni, harda yazilmasindan
# asili olmayaraq yenede isleyecekler. Ancaq, mentiqi ardicilliq olsa daha yaxsi olar.
masin.xoda_salmaq().surmek().masini_saxlamaq().masini_sondurmek()