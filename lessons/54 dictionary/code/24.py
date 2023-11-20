# update() metodu ile dictionary icerisinde var olan melumatlari yenilemek mumkundur.

melumatlar = {
  "istehsalatci": "Renault",
  "model": "Clio",
  "il": 2009
}

melumatlar.update(  {"il" : 2010}  )

print(melumatlar)
