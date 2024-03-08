import pandas as pd

melumatlar = {  
                'Name':   ['Alice', 'Bob', 'Charlie', 'Dave'],
                'Age':    [25, 30, 35, 40],
                'Salary': [50000, 60000, 70000, 80000],
            }

df = pd.DataFrame(melumatlar)  
print(df)

print('***********************************************************')


secilen_setr = df.loc[df['Age'] > 30, 'Redaktor'] = 'Islam'
print(secilen_setr)
#! Eger bele bir sutun movcud deyildirse bu adda sutun yaradilacaq ve gosterilen deyer hemin sutuna verilecek.
print(df)



















# melumatlar.loc[  melumatlar['Bonus %'] == 0, "GetBonus"  ] = "no bonus"
# melumatlar.loc[  melumatlar['Bonus %'] >  0, "GetBonus"  ] = "bonus"
# print(  melumatlar.head(10)  )


