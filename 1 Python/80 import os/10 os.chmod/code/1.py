# chmod - change mod sozunun qisaldilmasidir. Yeni, modu deyismek ucun istifade edilir.

# Bu asagida gorduyunuz xeta o vaxt baw verir ki, siz hal-hazirda oldugunuz faylin 
# icinden diger fayla muraciet etme huququna sahib deyilsiz. 

# Bu huququ elde etmek ucun emeliyyat sisteminin terminal penceresinde bu cur qeyd
# etmelisiniz ki, hemin huquqa sahib olasiz: chmod +x /Users/proj/domains/PYTHON/main.py


import os, stat

file_path = '/Users/proj/domains/PYTHON/main.py'

try:
    os.chmod(file_path, stat.S_IREAD | stat.S_IWRITE)  # oxuma və yazma icazəsi
    print("Fayla oxuma və yazma hüquqları uğurla verildi")

except OSError as e:
    print(f"Oxuma/yazma hüququnu dəyişmə xətası: {e}")

