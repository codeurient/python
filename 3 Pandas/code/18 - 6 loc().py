import pandas as pd

melumatlar = pd.read_excel('Datasets-main/ESD.xlsx')


#!  'GetBonus' adli sutun movcud olmadigi ucun ilk once yaradilir sonra ise asagida gosterilen deyerler 
#!  qoşduğumuz şərtə əsasən sətirlərə yazdırılır.
melumatlar.loc[  melumatlar['Bonus %'] == 0, "GetBonus"  ] = "no bonus"
melumatlar.loc[  melumatlar['Bonus %'] >  0, "GetBonus"  ] = "bonus"
print(  melumatlar.head(10)  )




















