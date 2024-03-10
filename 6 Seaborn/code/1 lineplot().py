# Seaborn() Seaborn Python proqramlaşdırma dili üçün statistik məlumatların vizuallaşdırılmasında istifade edilen kitabxanadır. 
# O, Matplotlib kitabxanasına əsaslanır və daha cəlbedici və informativ süjetlər yaratmağı asanlaşdıran interfeys təqdim edir.

# lineplot() funksiyasindan xətti diaqram yaratmaq üçün istifadə olunur.

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Days" : [1,2,3,4,5],
    "NOP"  : [50,40,60,30,44],
}

df = pd.DataFrame(data)
print(df)


sns.lineplot(data=data, x = "Days", y = "NOP")

plt.show()



#! https://github.com/mwaskom/seaborn-data