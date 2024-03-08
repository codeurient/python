import pandas as pd

data = pd.read_excel('Datasets-main/ESD.xlsx')

print(data)


# Hansi olkede MAX illik gelir elde edilir onun statistikasini aninda elde edirik.
qruplanmis_df = data.groupby(['Country']).agg(  { "Annual Salary" : 'max'}  )

print(qruplanmis_df)