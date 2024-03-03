import math

ad = input("Telebenin adini daxil edin: ")
eded1 = abs(  float( input("Kesir eded daxil edin: ") )  )
eded2 = abs(  int( input("Tam eded daxil edin: ") )  )

enBoyukEded = max( eded1, eded2 )
enKicikEded = min( eded1, eded2 )

yuxariYuvarlaqlasanEded = math.ceil(enBoyukEded)
asagiYuvarlaqlasanEded = math.floor(enKicikEded)

yuxariYuvarlaqlasanEded //= asagiYuvarlaqlasanEded

umumiMelumatlar = "Telebenin adi: " + ad + ",  Bu hesablamanin cavabi beledir: " + str(math.sqrt(pow(yuxariYuvarlaqlasanEded, 5)))

dilimlenmisInfo = slice(9, 13)
evezEdilen = umumiMelumatlar[dilimlenmisInfo]
evezEden = " ismi"

deyisdirilmisInfo = umumiMelumatlar.replace(evezEdilen, evezEden)

print( deyisdirilmisInfo  )