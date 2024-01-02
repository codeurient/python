# Klaslar arasinda multi qohumluq elaqeleri.
# It adli klas Heyvan adli klasi, Heyvan adli klas ise Canli adli klasi izleyir.
#//! It -> Heyvan -> Canli

class Canli:
    yasamaq = True

class Heyvan(Canli):
    def yemek(self):
        print("Bu heyvan yemek yeyir")

class It(Heyvan):
    def hurmek(self):
        print("Bu it hurur")

# Heyvan klasi Canli klasini izlediyi ve It klasi ise Heyvan adli klasi izlediyi
# ucun It klasi ile Canli klasi arasinda da bir elaqe qurulmuw olur ve Canli 
# klasinin xasseleri yaxud metodlari It klasi ucunde istifade edile biler.
        
it = It()
print(it.yasamaq)
it.yemek()