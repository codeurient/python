import pandas as pd

melumatlar = {  
                'Name':   ['Alice', 'Bob', 'Charlie', 'Dave'],
                'Age':    [25, 30, 35, 40],
                'Salary': [50000, 60000, 70000, 80000],
            }

df = pd.DataFrame(melumatlar)  
print(df)

print('***********************************************************')


#! Indeksi 1 olan setrin 'Name' adli sutunun deyerini elde edirik.
secilen_setr = df.loc[1, 'Name']
print(secilen_setr)





















# melumatlar.loc[  melumatlar['Bonus %'] == 0, "GetBonus"  ] = "no bonus"
# melumatlar.loc[  melumatlar['Bonus %'] >  0, "GetBonus"  ] = "bonus"
# print(  melumatlar.head(10)  )


