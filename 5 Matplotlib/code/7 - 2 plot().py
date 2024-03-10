import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('Datasets-main/expense3.xlsx')
df = pd.DataFrame(data)
qrup_data = df.groupby('Category')['Amount'].sum()

plt.plot(  qrup_data.index.astype(str),   qrup_data.values  )
plt.show()