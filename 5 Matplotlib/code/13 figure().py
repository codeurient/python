# figure() diaqram ölçüsünü göstərmək üçün istifadə olunur.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [45, 67, 33, 67, 12]
y1 = [41, 60, 13, 66, 13]

# 3 genislik 4 hundurluk
plt.figure( figsize=[3, 4] )

plt.plot(   x,   y   )
plt.plot(   x,   y1   )
plt.show()      