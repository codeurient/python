# dictionary comprehension - lüğət anlayışı - {}

#?  dictionary = { key: expression      for (key, value) in     iterable  }


# Fahrenhayt istilik olcme vahididir. Fahrenhayt gore suyun donma derecesi 32 qaynama derecesi ise 212-dir.
# Bu dustr ile Fahrenhayt olcu vahidinin bizim oyresmis oldugumuz derece cevirmek olar: (x-32) * (5/9)
seher_temp_fahrenheit_ile = {'Baki': 32, "Qax": 75, "Seki": 100, "Oguz": 50}


# items() metodu dictionary {} icinden "acar sozleri" ve "deyerleri" alaraq for dongusunde olan "acar" ve "deyer"
# parametr-lerine gonderir. En yuxarda yazmis oldugumuz dustura esasen formalasdiririq bu kodu.
seher_temp_derece_ile = {acar: round((deyer-32)*(5/9)) for (acar, deyer) in seher_temp_fahrenheit_ile.items()}

print(seher_temp_derece_ile)