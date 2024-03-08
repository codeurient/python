import pandas as pd

melumatlar = {  
                'Name':   ['Alice', 'Bob', 'Charlie', 'Dave'],
                'Age':    [25, 30, 35, 40],
                'Salary': [50000, 60000, 70000, 80000],
            }

df = pd.DataFrame(melumatlar)  
print(df)

print('***********************************************************')


secilen_setr = df.loc[df['Age'] > 30, 'Name'] = 'Islam'
print(secilen_setr)
#! Yasi 30-dan boyuk olan Name sutunundaki deyerlere = 'Islam' deyerini ver. 
print(df)



















# melumatlar.loc[  melumatlar['Bonus %'] == 0, "GetBonus"  ] = "no bonus"
# melumatlar.loc[  melumatlar['Bonus %'] >  0, "GetBonus"  ] = "bonus"
# print(  melumatlar.head(10)  )


