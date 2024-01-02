# Eger subklas-da ve ana klas-da eyni metod adi olarsa, ve biz subklas-i
# cagirdigimiz zaman hemin oxsar metod adindan istifade ederikse onda
# ustunluk subklas-in metod adina verilecekdir.

# yemek() metodu hem burda hem subklasda vardir.
class Heyvan:
    def yemek(self):
        print("Bu heyvan yemek yeyir")

# yemek() metodu hem burda hem ana klasda vardir.
class Dovsan(Heyvan):
    def yemek(self):
        print("Bu dovsan markov yeyir")

# dovsan subklasinin obyektini yaradaraq yemek() metodunu cagirsaq 
# hemin subklasda yaratmis oldugumuz metod adi esas goturulecekdir.  
dovsan = Dovsan()
dovsan.yemek()