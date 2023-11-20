# kvadrat moterize evezine dict-in value() metodundan istifade ederek de deyerleri elde etmek mumkundur

# Ilk once dict-e muraciet etmek lazimdir. Bizim dict-imizin adi 'melumatlar'-dir.

# Sonra .value() metodu ile butun deyerleri elde edirik ve for-in dongusunden istifade ederek
# x variable-ina hemin deyerleri gonderirik. 

# Artiq x icerisinde acar sozler yox deyerler olacaqdir ve hemin deyerleri ekrana yazdirmaq ucun
# print(x) demek kifayetdir.


melumatlar = {
  "istehsalatci": "Renault",
  "model": "Clio",
  "il": 2009
}

for x in melumatlar.values():
  print(x)