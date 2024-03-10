# color_palette() funksiyasi rəng palitralarını yaratmaq üçün istifadə olunur. 


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('Datasets-main/ESD.xlsx')
print(data)

color = sns.color_palette('GnBu')
sns.lineplot(data=data, x = "Business Unit", y = "Age",  hue="Gender",  palette = color)
plt.show()