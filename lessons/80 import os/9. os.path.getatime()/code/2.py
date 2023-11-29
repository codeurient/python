# eger fayl yaxud qovluq movcud deyilse xeta mesaji alariq


import os
import time

faylin_yolu = '/Users/proj/domains/PYTHON/asdasdasdsa.txt'

# Получение времени последнего доступа к файлу
giris_vaxti = os.path.getatime(faylin_yolu)

saat_formatinda_elde_et = time.ctime(giris_vaxti) 

print(  saat_formatinda_elde_et  )
