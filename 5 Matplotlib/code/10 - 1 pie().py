# pie() metodu, məlumatları dairə şəklində təmsil edən diaqramı yaratmaq üçün istifadə olunur

import matplotlib.pyplot as plt

brands = ["Oneplus", "Apple", "Samsung", "Nokia", "Redmi"]
x      = [22, 35, 30, 3, 10]
c      = ["red", "Violet", "blue", "magenta", "orange"]
ex     = [0, 0, 0, 0, 0.1]


plt.pie(  x,   labels=brands,   colors=c,    explode=ex,    shadow=True,    autopct="%.2f",   startangle=180 )
plt.show()