import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('Datasets-main/ESD.xlsx')
df = pd.DataFrame(data)

plt.hist(df['Age'],  bins=4,   edgecolor='black',    color='pink')
plt.show()