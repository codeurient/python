def duzeld(n):
    if 999 < n < 10000:
        n = (n // 1000) * 100 + (n % 100)
    return n

verilen_say = int(input("Verilen say: "))

if verilen_say > 99:
    duzeldilmis_say = duzeld(verilen_say)
    print("Verilen Say:", verilen_say)
    print("Düzeltilmiş Say:", duzeldilmis_say)
else:
    print("Xeta: Giris 99-dan kicik ola bilmez. 99 yaxud daha boyuk bir say girin.")
