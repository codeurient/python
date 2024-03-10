# 

import matplotlib.pyplot as plt

y = [98, 67, 88, 95, 88, 100]
x = ['Part1', 'Part2', 'Part3', 'Part4', 'Part5', 'Part6']

plt.bar(x, y)

# xlabel() - X oxuna etiket əlavə etmək üçün istifadə olunur
plt.xlabel("Parts of Movie")

# ylabel() - Y oxuna etiket əlavə etmək üçün istifadə olunur
plt.ylabel("Populatity")

# Diaqrama basliq metni əlavə etmək üçün istifadə olunur
plt.title("Populatity of Different parts of Movie")

plt.show()