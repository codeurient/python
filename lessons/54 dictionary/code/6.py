# dict icindeki butun deyerleri elde etmek ucun for - in dongusunden istifade etmek olar

# Deyerleri elde etmek ucun ilk novbede dict-i cagirmaq lazimdir.
# Sonra dict-in onunde kvadrta moterize qoyuruq. 
# Moterizenin icinde acar sozleri yazmaq lazimdir.
# Butun acar sozler for-in dongusu vasitesi ile x variable-ina verilir 
# Hemin x variable-ini kvadrat moterize icinde yazdiqda eslinde acar sozleri yazmis oluruq
# Belelikle butun deyerleri elde etdik


melumatlar = {
  "istehsalatci": "Renault",
  "model": "Clio",
  "il": 2009
}

for x in melumatlar:
  print(melumatlar[x])