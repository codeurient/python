import pandas as pd

melumatlar = pd.read_excel('Datasets-main/practice_2.xlsx')
print(  melumatlar  )

print('****************************************************************')

# Aldigi maasin 20 faizi miqdarinda bonus yaziriq.
melumatlar['Bonus'] = ( melumatlar['Salary'] / 100 ) * 20
print(  melumatlar  )