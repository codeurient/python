# python-da bir funksiyanin icinde onun ozunu cagira bilersiz. Buna recursive funksiya deyiller.
# Yeni oz-ozunu cagiran funksiya. Diqqetle qulaq asin cunki basa salan olmasa basa dusmek cetindi.

# Bu funksiyanin colunde rekursiv() funksiyasini 1 defe cagirmisiq ve deyer olaraq 7 ededini 
# vermisik: rekursiv(7). Bu cagrilma sadece 1 defe bas verir. 

# Sonra ise hemin funksiyanin icinde 2ci defe yeniden onun ozunu cagiririq. Bu icinde cagrilan funksiya 
# ise 1 den cox tekrarlanir, cunki deyer her defe deyisir. 

# Yeni, 1ci defe colde cagiranda 7 dedik, icerde cagiranda ise rekursiv(7 - 1) demis oluruq ve cavab 6 edir.
# 6 yeni eded oldugu ucun hemin icerideki funksiya yeniden isleyir ve bu kes rekursiv(6 - 1) demis oluruq 
# ve cavab 5 olur ve belece 0 (sifira) qeder deyerler cixila-cixila azalir.


# 7 + rekursiv(7 - 1) + rekursiv(6 - 1) + rekursiv(5 - 1) + rekursiv(4 - 1) + rekursiv(3 - 1) + rekursiv(2 - 1) + rekursiv(1 - 1) = 28

# En sonda netice olaraq 28 ededini elde edirik.

# Bes indi bu 1,3,6,10,15,21,28 nedir ? Sonraki sekile bax. Izahi orda.

def rekursiv(k):
  
  if(k > 0):
    netice = k + rekursiv(k - 1)
    print(netice)

  else:
    netice = 0
  return netice

rekursiv(7)




