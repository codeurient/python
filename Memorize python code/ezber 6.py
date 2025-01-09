import math
import time

siyahi = [
    "remove metodu list-in deyerini silir",     "Telebenin adini daxil edin: ",             "Kesir eded daxil edin: ", 
    "Tam eded daxil edin: ",                    ",  Bu hesablamanin cavabi beledir: ",      "Telebenin adi: ",
    "Sen bizim qrupun telebesi deyilsen",       " ismi",                                    "Yasar",                    "Harun",        "Amil"
]

siyahi.remove("remove metodu list-in deyerini silir")
siyahi.pop(9)
siyahi.append("Harun")
siyahi.insert(9, "Sahin")

ad = ''
while len(ad) == 0:
    ad = input(siyahi[0])

eded1 = ''
while not eded1:
    eded1 = abs(  float( input(siyahi[1]) )  )

eded2 = None
while not eded2:
    eded2 = abs(  int( input(siyahi[2]) )  )

enBoyukEded = max( eded1, eded2 )
enKicikEded = min( eded1, eded2 )
yuxariYuvarlaqlasanEded = math.ceil(enBoyukEded)
asagiYuvarlaqlasanEded = math.floor(enKicikEded)
yuxariYuvarlaqlasanEded //= asagiYuvarlaqlasanEded
metninYarisi = siyahi[3] + str(math.sqrt(pow(yuxariYuvarlaqlasanEded, 5)))

for say in range(1, 4):
    print(say)
    time.sleep(1)

if ad == siyahi[7]:
    umumiMelumatlar = siyahi[4] + ad + metninYarisi
elif ad == siyahi[8]:
    umumiMelumatlar = siyahi[4] + ad + metninYarisi
elif ad == siyahi[9]:
    umumiMelumatlar = siyahi[4] + ad + metninYarisi
else:
    print(siyahi[5])
    exit()

dilimlenmisInfo = slice(9, 13)
evezEdilen = umumiMelumatlar[dilimlenmisInfo]
evezEden = siyahi[6]
deyisdirilmisInfo = umumiMelumatlar.replace(evezEdilen, evezEden)
print( deyisdirilmisInfo  )


