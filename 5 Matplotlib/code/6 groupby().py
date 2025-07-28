import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel( "Datasets-main/expense3.xlsx" )
df = pd.DataFrame(data)
print(df.head(5))
print('***************************************************************')


# df.groupby("Payment Mode") - metodu ile "Payment Mode" sutununundaki elementleri qruplasdiririq.
# ["Amount"] - sutunu onu bildiririk, qruplasan informasiya ucun 'Amount' yəni meblegi esas gotur ve sum() metodu ile cemle.
qruplasdirilmis_data = df.groupby("Payment Mode")["Amount"].sum()
print(qruplasdirilmis_data)

# X oxuna index, Y oxuna value veririk ve neticeni diaqramda eks etdiririk.
plt.bar(  qruplasdirilmis_data.index,  qruplasdirilmis_data.values  )
plt.show()  