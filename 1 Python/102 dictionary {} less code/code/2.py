# dictionary comprehension [ˌkämprəˈhen(t)SH(ə)n]    -    lüğət anlayışı - {}

#?   dictionary = { key: expression        for (key, value) in        iterable if conditional }


hava = {'Baki': 'qarli', "Qax": 'gunesli', "Seki": 'gunesli', "Oguz": 'buludlu'}

# if şərti ilə sadece gunesli olan bolgelerin elde edilmesi.
gunesli_hava = {acar: deyer                        for (acar, deyer) in hava.items()                           if deyer == 'gunesli'}

print(gunesli_hava)