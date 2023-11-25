# funksiyanin parametr-leri necedenedirse o qederde deyeri olmalidir. Eks halda xeta alariq.

# Verilecek deyer sayi yaxud parametr sayi bilinmirse onda funksiyani yaradan zaman parametrin onune
# ulduz * simvolu qoymaq lazimdir.



def hesabla(*parametr): # Bu parametrin tipi tuple-dir.
    cem = 0
    for eldeEdilenDeyerler in parametr:
        cem += eldeEdilenDeyerler   # 4 + 6 + 2 + 4 + 3 + 8 + 5 + 4 = 36
    return cem

print(  hesabla(4,6,2,4,3,8,5,4)  )
