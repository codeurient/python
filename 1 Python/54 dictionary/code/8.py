# Eger hem 'acar sozleri' hemde 'deyerleri' eyni vaxtda elde etmek isteyirikse onda items() metodundan istifade
# ede bilerik.

# for -dan sonra 2 variable yaziriq x ve y. 
# x-a acar sozler, y-a ise deyerler avtomatik olaraq verilecekdir.

melumatlar = {
  "istehsalatci": "Renault",
  "model": "Clio",
  "il": 2009
}

for x, y in melumatlar.items():
  print(x, y)