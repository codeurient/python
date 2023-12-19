# replace() metodundan fayli yaxud qovlugu bir yerden basqa yere kocurmek ucun istifade edirik

import os

fayl = "test.txt"

teyinat = "/Users/proj/domains/PYTHON/numune/test.txt"

if os.path.exists(teyinat):
    print("Bele bir fayl artiq movcuddur.")
else:
    os.replace(fayl, teyinat)
    print("Fayl ugurla kocuruldu")