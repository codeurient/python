import pandas as pd

data = pd.read_excel('Datasets-main/ESD.xlsx')

print(data)

# Birden cox sutunu qruplasdirmaq mumkun oldugu kimi, agg() metodu ile birden cox funksinalliqda elave 
# etmek mumkundur.
qruplanmis_df = data.groupby(['Country', 'Gender']).agg(  { 'Annual Salary' : 'max', 'Age' : 'min'}  )

print(qruplanmis_df)