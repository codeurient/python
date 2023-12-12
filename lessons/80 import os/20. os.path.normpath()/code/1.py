# normpath() - normaya uygun yazilmayan yollari duzelderek normal veziyyete getirir.

# Meselen: asagida yazilan yolda bele bir hisse var "proj/.."
# Bu o demekdir ki, proj qovlugunun icine daxil ol sonra ise bir qovluq geri cix. Bu geri cix deyen 
# ../ iki noqte ve slesh simvoludur. 

# proj/../domains - Burda proj qovlugunun icinde domains qovlugu var. Biz ise burda ne demisik ?
# proj qovluguna daxil ol sonra bir addim geri cix sonra yeniden proj qovlugunun icinde olan domains
# qovluguna daxil ol. Eger proj qovlugundan geri cixiramsa artiq nece domains qovluguna daxil ola bilerem ?
# Bu mentiqsizlikdir ve bele mentiqsizlikleri duzeltmek ucun normpath() metodundan istifde edilir.

# Bu metod ../ tek bu simvolu yox ozu ile proj/.. diger yoluda silir. Eger lazim olarsa kod yazaraq
# hemin lazim olan ancaq silinmiw hisseni geri yazadira bilerik. 

import os

faylin_yolu = 'Users/proj/../domains/./PYTHON/test.txt'

fayl_haqqinda = os.path.normpath(faylin_yolu)
print(  fayl_haqqinda  )