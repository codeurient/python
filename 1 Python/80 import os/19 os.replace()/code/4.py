# replace() metodundan fayli yaxud qovlugu bir yerden basqa yere kocurmek ucun istifade edirik

import os

fayl = "test2"

teyinat = "/Users/proj/domains/PYTHON/numune/test2"

if os.path.exists(teyinat):
    print("Bele bir fayl artiq movcuddur.")
else:
    os.replace(fayl, teyinat)
    print("Fayl ugurla kocuruldu")