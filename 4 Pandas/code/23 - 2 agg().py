import pandas as pd

data = pd.read_excel('Datasets-main/ESD.xlsx')

print(data)


#  Departmen sutununda birden cox ferqli alt sobe var:
# 1) Accounting
# 1) Engineering
# 1) Finance
# 1) Human Resources ve.s

# groupby() funksiyasi ile ilk once hemin alt sobeleri qruplasdiririq sonra count() metodu ile saylarini elde edirik.
# "Gender" hemin cedvelin sütun adıdır və biz burda sadəcə bu sütunun sayısını əldə edirik.
qruplanmis_df = data.groupby('Department').agg(  { "Gender" : 'count'}  )

print(qruplanmis_df)