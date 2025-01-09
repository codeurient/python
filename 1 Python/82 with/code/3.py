# Eger acmaq ve icini oxumaq istediyimiz fayl movcud deyilse xeta mesaji almamaq ucun try-except
# konstruksiyasindan istifade edirik.

try:
    with open('test2.txt') as sened:
        print(sened.read())
except FileNotFoundError:
    print("Bele bir fayl movcud deyil")