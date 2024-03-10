# bar() funksiyasi bar diaqramı (histoqram) yaratmaq üçün istifadə olunur. İki mecburi arqument qebul 
# edir: X oxu dəyərlərinin siyahısı və Y oxu dəyərlərinin siyahısı

import matplotlib.pyplot as plt

y = [98, 67, 88, 95, 88, 100]
x = ['Part1', 'Part2', 'Part3', 'Part4', 'Part5', 'Part6']

# y oxu deyerleri x oxu deyerleri ile ust uste dusmelidir. 
plt.bar(x, y)

# Yaranan diaqrami gostermek ucun show() metodundan istifade edilir.
plt.show()