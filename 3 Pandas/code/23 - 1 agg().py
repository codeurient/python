# agg() - funksiyası, qruplaşdırılmis nəticələrin üzərində birden cox ferqli əməliyyatlar tətbiq etmək üçün 
# istifadə olunur. 

import pandas as pd

data = {
            'Qrup':  ['A', 'B', 'A', 'B', 'A'],
            'Deyer': [10,  20,  30,  40,  50 ]
        }

df = pd.DataFrame(data)

# 'sum' ve 'mean' funksiya adlaridir.
qruplanmis_df = df.groupby('Qrup').agg(  {'Deyer' : ['sum', 'mean']}  )

# Oxşar verilənlər bir qruplaşdı.

#        sum  mean
# Qrup            
# A       90  30.0
# B       60  30.0
print(qruplanmis_df)