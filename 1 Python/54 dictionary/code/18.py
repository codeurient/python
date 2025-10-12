# dict() metodundan da istifade ederek 1 dictionary-ni basqa bir variable-a kopyalamaq mumkundur 


melumatlar = {
  "istehsalatci": "Renault",
  "model": "Clio",
  "il": 2009
}

yeniMelumatlar = dict(melumatlar)

yeniMelumatlar['il'] = 2010

print(melumatlar)
print(yeniMelumatlar)