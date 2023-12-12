# os.path.join() - bu metod ile join() metodunu sehf salmayarsiniz. Cunki 2 ferqli metoddur.hasattr

# os.path.join() - bu metod string tipinde yazilan deyerleri birlewdirerek fayl yaxud qovluq
# yolu yaradir.

# Mac ve Windows emeliyyat sistemlerinde fayl ve qovluq yollari ferqli olur. Yeni slesh simvolu
# ferqli dayana biler. Meselen:
# Mac:      Users/proj/domains/PYTHON/test.txt
# Windows:  Users\proj\domains\PYTHON\test

# Bu metod ise proqramin iwe salindigi emeliyyat sisteminden asili olaraq avtomatik wekilde deyerleri 
# yol formatina salir.

import os


fayl_haqqinda = os.path.join('Users', 'proj', 'domains', 'PYTHON', 'test.txt')

print(  fayl_haqqinda  )