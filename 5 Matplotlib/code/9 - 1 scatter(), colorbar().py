# scatter() funksiyası səpələnmə qrafası yaratmaq üçün istifadə edilir.

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1, 10, 50)
y = np.random.randint(1, 100, 50)
color = np.random.randint(10, 100, 50)
size = np.random.randint(10, 100, 50)


# 1) cmap = "viridis"    ve   c = color     arqumentleri birlikde istifade edilir.
# 2) cmap = "viridis" arqumenti, evvelceden teyin edilmis renglerdir.
# 3) c = color        arqumenti, qrafikdəki hər bir nöqtənin rəngini müəyyən edir. Bu, rengler cmap (color map)
# arqumentinden goturulur. 
plt.scatter(x,  y,  marker = "*",  cmap = "hot",  c = color, s = size)
plt.colorbar()
plt.show()