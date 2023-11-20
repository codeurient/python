# update() metodu ile 2 ferqli dictionary elementlerini birlesdirmek mumkundur

# Burda "melumat2"-ni "melumat1" ile birlesdiririk.

# Yeni, "melumat1" variable-i yenilenir.

# Eger eyni acar sozler olarsa onda "meulmat1" icindeki deyerler "meulmat2" icindeki deyerler ile 
# evez edilecekdir. 

melumat1 = {'a': 1, 'b': 2}
melumat2 = {'b': 3, 'c': 4}

melumat1.update(melumat2)

print(melumat1)
print(melumat2)