# Bu metod emeliyyat sisteminin Disk adi ile kataloq adini 2 hisseye 
# ayirmaq ucun istifade edilir. 

# Mac emeliyyat sistemlerinde Windows-da oldugu kimi Disk anlayiwi olmadigi
# ucun bu metod Mac emeliyyat sistemi ucun tetbiq edilmir.


import os

yol = '/Users/proj/domains/PYTHON/test.txt'

qovluq, fayl = os.path.splitdrive(yol)

print("Qovluq:", qovluq)  
print("Faylin adi:", fayl)  