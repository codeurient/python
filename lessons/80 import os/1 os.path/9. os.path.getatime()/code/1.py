# getatime() - bu metod her hansisa bir fayla yaxud qovluga en son edilen muracietin tarixini qaytarir

# 1) Eger faylin yaxud qovlugun icinde deyisiklik edilibdirse onda tarix yenilene biler
# 2) Eger fayl yaxud qovlug her hansisa proqram terefinden acilibdirsa onda tarix yenilene biler
# 3) Bezi fayllar emeliyyat sistemi terefinden avtomatik olaraq yenilene bilir, yeni 
# emeliyyat sistemi o faylin icerisine nelerse elave ede biler yaxud her hansisa bir fayli acaraq
# ordan melumat kopyaliya biler. Hemin bu prosedur vaxtida tarix yenilenmesi bas verir ve 
# biz belelikle fayla yaxud qovluga mudaxile edilib edilmediyini oyrenirik.

# Bunu test etmek ucun test.txt faylini phpstorm proqrami ile acdiqdan sonra asagidaki kodlari
# iwe salaraq yeni yaranan tarixi gore bilerik.

import os
import time

faylin_yolu = '/Users/proj/domains/PYTHON/test.txt'

# Получение времени последнего доступа к файлу
giris_vaxti = os.path.getatime(faylin_yolu)

saat_formatinda_elde_et = time.ctime(giris_vaxti) 

print(  saat_formatinda_elde_et  )


