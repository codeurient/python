import math

eded1 = abs(  float( input("Kesir eded daxil edin: ") )  )
eded2 = abs(  float( input("Kesir eded daxil edin: ") )  )
eded3 = abs(  float( input("Kesir eded daxil edin: ") )  )
eded4 = abs(  float( input("Kesir eded daxil edin: ") )  )
eded5 = abs(  float( input("Kesir eded daxil edin: ") )  )

enBoyukEded = max( eded1, eded2, eded3, eded4, eded5)
enKicikEded = min( eded1, eded2, eded3, eded4, eded5)

yuxariYuvarlaqlasanEded = math.ceil(enBoyukEded)
asagiYuvarlaqlasanEded = math.floor(enKicikEded)

hasil = yuxariYuvarlaqlasanEded * asagiYuvarlaqlasanEded

print(  math.sqrt(  pow(hasil, 5)  )  )