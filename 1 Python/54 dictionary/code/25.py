# update() metodu ile dictionary icerisine yeni melumatlar da elave etmek mumkundur

melumatlar = {
  "istehsalatci": "Renault",
  "model": "Clio",
  "il": 2009
}

melumatlar.update(  {"reng" : "qirmizi"}  )

print(melumatlar)