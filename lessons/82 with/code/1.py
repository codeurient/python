# open() bu metod gosterilen fayli acmaq ucun istifade edilir


# with konstruksiyadir ve fayli acildiqdan sonra avtomatik olaraq baglamaq ucun istifade edilir.


# Eger bu konstruksiya olmasa idi onda close() metodu ile ozumuz manual baglamaq mecburiyyetinde qalardiq.


# Fayl acildiqdan sonra hemin fayli "as sened" deyerek sened variable-ina gonderirik ve print() metodu 
# ile hemin variable-in adindan istifade ederek fayli ekrana yazdirirq.

with open('test.txt') as sened:
    print(sened)