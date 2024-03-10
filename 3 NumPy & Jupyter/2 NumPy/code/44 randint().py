# randint() metodu random ededler elde etmek ucun istifade edilir
# 1ci parametr - start
# 2ci parametr - stop
# 3cu parametr - size

import numpy as np

# 1 ile 10 arasinda 50 dene random eded elde edirik.
x = np.random.randint(1, 10, 50)


print(x)