# Burda exists() metodu ile bele bir yolun movcud olub olmadigini yoxlayiriq.

# isfile() metodu ile hemin gosterilen yolun fayl olub olmadigini yoxlayiriq

# isdir() metodu ile hemin gosterilen yolun qovluq olub olmadigini yoxlayiriq

# Eger bu sorgular FALSE vererse en sonda olan else kodu ekrana bir mesaj yazdiracaqdir

import os

yol = "/Users/proj/domains/PYTHON"
# yol = "C:\\Users\\Cakow\\Desktop\\test.txt"

if os.path.exists(yol):
    print("Bele bir yol movcuddur")
    if os.path.isfile(yol):
        print("Bu bir fayldir")
    elif os.path.isdir(yol):
        print("Bu bir qovluqdur")
else:
    print("Bele bir yol movcud deyildir")