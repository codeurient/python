# bu metod emeliyyat sisteminin bezi xarakteristikalari haqqinda melumat elde etmek ucundur.

# Meselen

# sysname:  emeliyyat sisteminin adi
# nodename: duyum adi
# release:  emeliyyat sisteminin versiyasi - sadece versiyanin son tarixi
# version:  emeliyyat sisteminin versiyasi - adi ve son tarixi (yeni daha etrafli)
# machine:  platformanin adi

import os

melumat = os.uname()

for etrafliMelumat in melumat:
    print(etrafliMelumat)