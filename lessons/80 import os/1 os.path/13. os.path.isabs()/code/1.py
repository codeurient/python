# isabs() - bu metod faylin yaxud qovlugun yolunun mutleq (absolute) olub olmadigini teyin edir.
# Eger yol absolute yol olarsa bu metod TRUE eks halda FALSE qayidacaqdir.

# 2 cur yol vardir mutleq (absolute) yol ve nisbi (relative) yol 

# 1) absolute yol, faylin yaxud qovlugun tam yolunu ifade edir. Tam yol ise bawlayir, 
# komputerin, emeliyyat sisteminin kökündən. Yeni: /Users/proj/domains/PYTHON/test.txt
# Windows emeliyyat sisteminde ise bele ola bilerdi: C:\Users\Username\Documents\test.txt

# 2) relative yol, faylin yaxud qovlugun hal hazirda yerlewmiw oldugu qovluga nisbeten olan yoludur.
# Melesen, test.txt yerlewir python qovlugunun icinde ve:  python/test.txt
# bu yol nisbi yol sayilir.


import os

faylin_yolu = '/Users/proj/domains/PYTHON/test.html'
# faylin_yolu = 'PYTHON/test.html'

fayl_haqqinda = os.path.isabs(faylin_yolu)

print(  fayl_haqqinda  )