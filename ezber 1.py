ad = input("Adinizi dail edin: ")
soyad = input("Soyadinizi dail edin: ")
yash = int(  input("Yasinizi daxil edin:")  )
boy = float(  input("Boyunuzu daxil edin")  )

evezEdilen = "adim"
evezEden = "ismim"

umumiMelumatlar = "Menim adim: " + ad + ", Soyadim: " + soyad + ", Yasim: " + str(yash) + ", Boyum: " + str(boy)

deyisdirilmisInfo = umumiMelumatlar.replace(evezEdilen, evezEden)

print(deyisdirilmisInfo)