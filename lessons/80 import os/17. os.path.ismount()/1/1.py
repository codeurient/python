# ismount() - bu metod mount nöqtəsinə qoşulmaq üçündür. Mount noqtesi yeni, montaj noqtesi nedir ? 

# Kompyuterlerde, emeliyyat sistemlerinde butun proqramlarin yerlewmiw oldugu bir qovluq vardir.
# Bu qovlugun icinde drayverler, usb cihazlar, yaddaw qurgulari, terminal pencere ve.s movcuddur.

# Eger komputere, emeliyyat sistemine tam sekilde mudaxile etmek isteyirikse onda hemin mount noqtesine
# daxil olmaliyiq. 

# Mac emeliyyat sisteminde /dev qovlugu mount noqtesidir
# Windows  emeliyyat sisteminde /Device yaxud C: diski mount noqtesidir. 

# Gosterilen yolun mount noqtesi olub olmadigini teyin etmek ucun ismount() metodundan istifade edilir.
# Eger yol mount noqtesi olarsa proqram true eks halda false qayatarar.

import os

faylin_yolu = '/dev'

fayl_haqqinda = os.path.ismount(faylin_yolu)
print(  fayl_haqqinda  )