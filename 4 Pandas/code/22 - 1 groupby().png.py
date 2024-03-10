# groupby() - funksiyası DataFrame-i qruplaşdırmaq üçün istifadə olunur. Bu funksiya verilənləri 
# müəyyən sütuna görə qruplaşdırır.

import pandas as pd

data = {
            'Qrup':  ['A', 'B', 'A', 'B', 'A'],
            'Deyer': [10,  20,  30,  40,  50 ]
        }



df = pd.DataFrame(data)


# 'Qrup' sütununa görə qruplaşdıraq və qrupların cənibi hesablayaq. 
# Verilənləri qruplaşdırdıqdan sonra onlarla bir əməliyyat icra etmək lazımdır.  Məsələn sum() metodu kimi.
gruplanmis_df = df.groupby('Qrup').sum()

# Oxşar verilənlər bir qruplaşdı.
    # Qrup       
    # A        90
    # B        60
print(gruplanmis_df)