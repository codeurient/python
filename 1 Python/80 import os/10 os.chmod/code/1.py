# chmod - change mod sozunun qisaldilmasidir. Yeni, modu deyismek ucun istifade edilir.

# Bu asagida gorduyunuz xeta o vaxt baw verir ki, siz hal-hazirda oldugunuz faylin 
# icinden diger fayla muraciet etme huququna sahib deyilsiz. 

# Bu huququ elde etmek ucun emeliyyat sisteminin terminal penceresinde bu cur qeyd
# etmelisiniz ki, hemin huquqa sahib olasiz: chmod +x /Users/proj/domains/PYTHON/main.py


import os, stat

try:
    os.chmod('/Users/proj/domains/PYTHON/main.py')
    print("Fayla muraciet etme huququ ugurla deyiwdirildi")

except OSError as e:
    print(f"Muraciet etme huququnu deyisme xetasi: {e}")
