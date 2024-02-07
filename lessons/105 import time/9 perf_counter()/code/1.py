import time

def yemek():
    print("Men yemek yeyirem")

# Funksiyani cagirana qeder vaxt tuturuq
baslama_vaxti = time.perf_counter()

# Funksiyani cagiririq
yemek()

# Funksiyani cagirdiqdan sonra yeniden vaxt tuturuq
bitme_vaxti = time.perf_counter()

# Funksiya cagrildiqda vaxt gedir deye, mentiqle bu daha uzun vaxt muudetidir.
# Funksiya cagrilmadiqda vaxti az gedir deye. mentiqle bu daha qisa vaxt muddetidir.
# Uzun vaxtdan cixiriq qisa vaxti ve kecen muudeti tapiriq.
icra_muddeti = bitme_vaxti - baslama_vaxti

print(icra_muddeti)
