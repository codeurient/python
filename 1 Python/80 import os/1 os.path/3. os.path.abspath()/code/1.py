# abspath() - bu metod ana qovlugun yolunu bize verir. 

# Mesel ucun main.py fayli yerlesir PYTHON qovlugunun icinde ve hemin bu qovlugun icinde
# de test.txt fayli var. 

# abspath() metodu hemin ana qovlugun adini bize verir: /Users/proj/domains/PYTHON/

# Biz sadece asagidaki kimi faylin adini yaziriq ve abspath() metodu avtomatik olaraq
# hemin qovlugun yolunu bu fayla elave edir. Belelikle faylin tam yolunu elde etmiw oluruq.

import os

yol = "test.txt"

print(   os.path.abspath(yol)   )