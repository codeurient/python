# chmod() metodu modu nece ve ne ucun deyisdirir ? 

# Buna misal ucun bayaq yazmis oldugumuz 2 numuneni gostermek olar.

# Yeni, bayaq python kod ile test.txt faylinin modunu deyismeye caliwdiq ancaq xeta mesaji aldiq.

# Ne etdik ? Emeliyyat sisteminin kodu olan 'chmod' kodundan istifade ederek hal-hazirda
# icinde oldugumuz fayldan test.txt faylinin modunu deyismek ucun icaze aldiq. 

# Bayaq yazdigimiz chmod ile bu faylin icinde yazmiw oldugumuz chmod() ferqli proqrama mexsus
# kodlardir. Biri emeliyyat sistemine aiddir digeri ise python proqram diline. Ancaq ikiside
# prinsip olaraq eyni iwi icra edirler. Yeni, mod deyiwdirmek ucun istifade edilirler. 

# Eger bir faylin icine yazi yazmaga icazemiz yoxdursa ve koddan istifade ederek yazi yazmaga caliwariqsa
# xeta mesaji ala bilerik. Cunki, icaze yoxdur. Icaze almaq ucun ise chmod() metodundan istifade edirik.

# Bu mod-lar ferqli-ferqli olur. Yeni, yazi yazdirmaq ayri mod, sadece faylin icini oxumaq ayri mod ve.s

import os, stat

try:
    os.chmod('/Users/proj/domains/PYTHON/test.txt', stat.S_IWRITE)
    print("Fayla muraciet etme huququ ugurla deyiwdirildi")

except OSError as e:
    print(f"Muraciet etme huququnu deyisme xetasi: {e}")
