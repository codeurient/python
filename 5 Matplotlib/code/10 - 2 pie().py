import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('Datasets-main/expense3.xlsx')
df = pd.DataFrame(data)
qrup_data = df.groupby("Payment Mode")["Amount"].sum()




plt.pie(  qrup_data.values,    labels = qrup_data.index,    autopct = '%.2f' )
plt.show()