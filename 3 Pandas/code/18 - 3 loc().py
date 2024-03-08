import pandas as pd

melumatlar = {  
                'Name':   ['Alice', 'Bob', 'Charlie', 'Dave'],
                'Age':    [25, 30, 35, 40],
                'Salary': [50000, 60000, 70000, 80000],
            }

df = pd.DataFrame(melumatlar)  
print(df)

print('***********************************************************')


#! Cedvelin 'Age' adli sutununda olan deyerler ucun şərt qosuruq ki, eger hemin sutunda olan deyerler 
#! 30-dan boyukdurse hemin deyerleri 'secilen_setr' adli variable-a ver. Belelikle hansilar ki, boyukdur onlari elde edirik.
secilen_setr = df.loc[df['Age'] > 30]
print(secilen_setr)




















# melumatlar.loc[  melumatlar['Bonus %'] == 0, "GetBonus"  ] = "no bonus"
# melumatlar.loc[  melumatlar['Bonus %'] >  0, "GetBonus"  ] = "bonus"
# print(  melumatlar.head(10)  )


