# savefig() metodu, diaqrami yadda saxlamaq ucun istifade edilir.

# Olcu arxaya reng vermek ve.s kimi ferqli emeliyyatlarda etemek mumkundur ancaq bunlari o qeder coxdur ki, tek-tek
# gostermek vaxt itkisidir. En yaxsi metodika ise hara baxmaq lazim oldugunu bilmekdir ki, bu saydiqlarimizi icra ede bilesiz.

import matplotlib.pyplot as plt

brands = ["Oneplus", "Apple", "Samsung", "Nokia", "Redmi"]
x      = [22, 35, 30, 3, 10]
c      = ["red", "Violet", "blue", "magenta", "orange"]
ex     = [0, 0, 0, 0, 0.1]


plt.pie(  x,   labels=brands,   colors=c,    explode=ex,    shadow=True,    autopct="%.2f",   startangle=180 )

plt.savefig('pie.png')

plt.show()