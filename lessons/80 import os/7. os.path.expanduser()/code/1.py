# expanduser() - bu metod emeliyyat sisteminin, istifadeci qovlugunun adini bize verir.

# Emeliyyat sistemlerinde bele bir simvol var ~ 
# Bu simvol en esas, en bawlangicda olan ana qovlugun yolunu nezerde tutur.

# Pythonda bu simvolu adi halda yol kimi gore bilmediyinden, expanduser() metodundan
# hemin simvolu, emeliyyat sisteminin istifadeci qovlugu adina cevirmek ucun istifade edilir.


import os

yol1 = "~"
yol2 = "~/Downloads"
yol3 = "~/folder/text.txt"

print(   os.path.expanduser(yol1)   )
print(   os.path.expanduser(yol2)   )
print(   os.path.expanduser(yol3)   )