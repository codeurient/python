# ismount() - bu metod mount nöqtəsinə qoşulmaq üçündür. Mount noqtesi yeni, montaj noqtesi nedir ? 

import os

faylin_yolu = '/dev'

fayl_haqqinda = os.path.ismount(faylin_yolu)
print(  fayl_haqqinda  )