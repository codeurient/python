# Baxin indi ise sadece "yeniMelumatlar" variable-ina muraciet ederek deyeri 2010 etdim 
# ve ne bas verdi ?

# "melumatlar" variable-ini print() etkdikde ekrana eyni neticeler yazdirildi.

# Bu o demekdir ki, "yeniMelumatlar" ve "melumatlar" eyni dictionary-dir.

melumatlar = {
  "istehsalatci": "Renault",
  "model": "Clio",
  "il": 2009
}

yeniMelumatlar = melumatlar

yeniMelumatlar['il'] = 2010

print(melumatlar)
print(yeniMelumatlar)