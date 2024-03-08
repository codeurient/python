import pandas as pd

data = pd.read_excel('Datasets-main/ESD.xlsx')

print(data)


# Birden cox sütun adı üçün də qruplaşdırmaq mümkündür.
qruplanmis_df = data.groupby(['Department', 'Gender']).agg(  { "EEID" : 'count'}  )

print(qruplanmis_df)