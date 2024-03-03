# istitle() - bu metod bir metnin basliq metni olub olmadigini yoxlayir

#  Eger bir cumlede her sozun bas herfi boyuk yazilarsa bu hemin cumlenin basliq metni oldugu menasina gelir ve bu metod
# true qaytarir.

basliqMetni1 = "Ac Əlinə Düşəni Yeyər, Tox Ağzına Gələni Deyər."
basliqMetni2 = "Ac Əlinə Düşəni yeyər, Tox Ağzına Gələni Deyər."

print(   basliqMetni1.istitle()   )
print(   basliqMetni2.istitle()   )