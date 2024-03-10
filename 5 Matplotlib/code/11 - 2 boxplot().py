import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_excel('Datasets-main/ESD.xlsx')
df = pd.DataFrame(data)
print(print(df['Annual Salary'].describe()))


plt.boxplot(df['Annual Salary'])
plt.show()