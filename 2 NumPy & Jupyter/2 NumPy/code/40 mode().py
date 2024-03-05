# mode() metodu, en cox tekrarlanan oxsar deyer hansidirsa onu elde etmek ucun istifade edilir.

# mode() metoduna parametr olaraq list yaxud array vermek olar. 

import numpy as np
import statistics as stats


qutu1 = [200, 300, 150, 130, 200, 280, 170]
#! yeni_qutu3 = np.array(qutu1)
print(  stats.mode(qutu1)  )                    # 200




qutu2 = [200, 150, 150, 150, 200, 280, 170]
#! yeni_qutu3 = np.array(qutu2)
print(  stats.mode(qutu2)  )                    # 150



# Eger tekrarlanma her deyer ucun eyni sayda olarsa onda en basda duran deyer esas goturulecekdir.
qutu3 = [150, 150, 150, 150,    200, 200, 200, 200,    170, 170, 170, 170 ]
#! yeni_qutu3 = np.array(qutu3)
print(  stats.mode(qutu3)  )                    # 150