# Bizim kodumuz "main.py" faylinin icindedir ve bu faylin yerlewmis oldugu qovlugun
# hansi oldugunu oyrenmek isteyirikse onda realpath() metodundan istifade ede bilerik.

# Bu metoddan, emeliyyat sisteminden bawlayaraq hemin kodun iwe salindigi yere qeder olan yolun tamamini
# elde etmek ucun istifade edilirir. Yeni absolute yeni mutleq yolu elde edirik.

# __file__  - icinde oldugumuz faylin adini elde etmek ucun, bu gorduyunuz xususi variable-dan 
# istifade edirik.

import os

fayl_haqqinda = os.path.realpath(__file__)
print(  fayl_haqqinda  )