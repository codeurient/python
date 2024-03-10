# islower() - bu metod ile simvolun kicik olub olmadigini yoxlayiriq

# ilk once ise indeksi 0 sifir olan simvolu cagirirq [0] 
# sonra ise if sorgusu vasitesi ile eger hemin simvol kicikdirse onda capitalize() 
# metodundan istifade ederek hemin simvolu boyuduruk


ad = "semed vurgun"

if(   ad[0].islower()   ):
    ad = ad.capitalize()
print(ad)