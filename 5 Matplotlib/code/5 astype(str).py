import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel( "Datasets-main/expense3.xlsx" )

df = pd.DataFrame(data)
print(df)

# Diaqramada cedvelden sadece 2 sutununa aid melumatlari gostereceyik.
# astype() metodu ile X oxuna verilecek melumatlarin tipini teyin edirik.
plt.bar(df["Payment Mode"].astype(str), df["Amount"])
plt.show()