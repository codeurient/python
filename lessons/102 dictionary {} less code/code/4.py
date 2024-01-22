# dictionary comprehension [ˌkämprəˈhen SH n]    -    lüğət anlayışı - {}

#?   dictionary = { key: function(value)      for (key, value) in iterable  }


seherler = {'Baki': 32, "Qax": 75, "Seki": 100, "Oguz": 50}

# Bundan evvelki neticeni oz funksiyamizi yazaraqda elde ede bilerik.
def havani_yoxla(deyer):
    if deyer >= 70:
        return "ISTI"
    elif 69 >= deyer >= 40:
        return "ILIQ"
    else:
        return "SOYUQ"  

seher_aciqlama = {acar: havani_yoxla(deyer) for (acar, deyer) in seherler.items()}

print(seher_aciqlama)