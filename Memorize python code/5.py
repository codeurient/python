import math
import time

ad = ''
while len(ad) == 0:
    ad = input("Telebenin adini daxil edin: ")

eded1 = ''
while not eded1:
    eded1 = abs(  float( input("Kesir eded daxil edin: ") )  )

eded2 = None
while not eded2:
    eded2 = abs(  int( input("Tam eded daxil edin: ") )  )

enBoyukEded = max( eded1, eded2 )
enKicikEded = min( eded1, eded2 )
yuxariYuvarlaqlasanEded = math.ceil(enBoyukEded)
asagiYuvarlaqlasanEded = math.floor(enKicikEded)
yuxariYuvarlaqlasanEded //= asagiYuvarlaqlasanEded
metninYarisi = ",  Bu hesablamanin cavabi beledir: " + str(math.sqrt(pow(yuxariYuvarlaqlasanEded, 5)))

for say in range(1, 4):
    print(say)
    time.sleep(1)

if ad == "Yasar":
    umumiMelumatlar = "Telebenin adi: " + ad + metninYarisi
elif ad == "Harun":
    umumiMelumatlar = "Telebenin adi: " + ad + metninYarisi
elif ad == "Sahin":
    umumiMelumatlar = "Telebenin adi: " + ad + metninYarisi
else:
    print("Sen bizim qrupun telebesi deyilsen")
    exit()

dilimlenmisInfo = slice(9, 13)
evezEdilen = umumiMelumatlar[dilimlenmisInfo]
evezEden = " ismi"
deyisdirilmisInfo = umumiMelumatlar.replace(evezEdilen, evezEden)
print( deyisdirilmisInfo  )


