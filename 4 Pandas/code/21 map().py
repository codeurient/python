import pandas as pd

melumatlar = { 'Month' : [ 'January', 'Feburary', 'March', 'April' ]}
yeni_deyer = pd.DataFrame(melumatlar)

print(yeni_deyer)
# 
def deyerler(deyer):
    # İndexing qaydasi ilə həmin dəyərlərin bir parçasını əldə edirik.
    return deyer[0:3]

# 
# Cedvelin icinde 'Short month' adinda yeni sütun yaradırıq.
# map() metodu ile cedvelin 'Month' adli sütununa müraciət edirik. map() metodu 
# 'January', 'Feburary', 'March', 'April' elementlerini tek-tek elde etmek ucun istifade edilir.
# By elementler 'deyerler' adli funksiyanin 'deyer' adli parametrine gonderilir.
# Yəni, 'deyer' parametri həm January həm Feburary həm March həm də April elementləridir. 
yeni_deyer['Short month'] = yeni_deyer['Month'].map(deyerler)

print(yeni_deyer)