# dictionary comprehension [ˌkämprəˈhen(t)SH(ə)n]    -    lüğət anlayışı - {}

#?   dictionary = { key: (if/else)      for (key, value) in iterable  }


seherler = {'Baki': 32, "Qax": 75, "Seki": 100, "Oguz": 50}

# if sorgusu ile sert qosaraq deyirik ki, eger derece 40 dan cox olarsa "deyer" olaraq ISTI ekse halda SOYUQ yazdir.
seher_aciqlama = {    acar: ("ISTI" if deyer >= 40 else "SOYUQ")                          for (acar, deyer) in seherler.items()      }

print(seher_aciqlama)