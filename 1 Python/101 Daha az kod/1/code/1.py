kvadrat = []

# range() metodu 1-den 11-e qeder sirasi ile ededler yaradir. (11 daxil deyil)
for i in range(1, 11):
    # for dongusu ile ededleri elde edir ve "i" variable-ina gonderirik. 
    # append() metodu icinde hemin ededleri bir birine vurur ve "kvadrat" adli "list"-in icine elave edirik.
    kvadrat.append(i * i)
    # 1 * 1
    # 2 * 2
    # 3 * 3
    # 4 * 4
    # 5 * 5
    # 6 * 6
    # 7 * 7
    # 8 * 8
    # 9 * 9
    # 10 * 10
print(kvadrat)