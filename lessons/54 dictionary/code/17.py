# Indi ise copy metodundan istifade ederek 1ci dictionary-i olan "melumatlar"-i kopyalayiriq
# "yeniMelumatlar" variable-ina. 

# Artiq 2 ferqli dictionary movcuddur. "melumatlar" ayri, "yeniMelumatlar" ayridir.

# Ferqi neticeni ekrana yazdiraraq gormek mumkundur.

melumatlar = {
  "istehsalatci": "Renault",
  "model": "Clio",
  "il": 2009
}

yeniMelumatlar = melumatlar.copy()

yeniMelumatlar['il'] = 2010

print(melumatlar)
print(yeniMelumatlar)