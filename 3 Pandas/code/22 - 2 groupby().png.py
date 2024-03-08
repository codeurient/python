import pandas as pd

data = pd.read_excel('Datasets-main/ESD.xlsx')

print(data)


# Mesel ucun, Departmen sutununda birden cox ferqli alt sobe var:
# 1) Accounting
# 1) Engineering
# 1) Finance
# 1) Human Resources ve.s

# groupby() funksiyasi ile ilk once hemin alt şöbeleri qruplasdiririq sonra count() metodu ile saylarini elde edirik.
qruplanmis_df = data.groupby('Department').count()

print(qruplanmis_df)