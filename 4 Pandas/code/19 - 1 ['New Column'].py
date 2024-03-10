import pandas as pd

melumatlar = pd.read_excel('Datasets-main/practice_1.xlsx')


yeni_cedvel =  melumatlar['Full Name'] = melumatlar['Name'].str.capitalize() + ' ' + melumatlar['Surname']

print(  melumatlar  )
print('****************************************************************')
print(  yeni_cedvel  )