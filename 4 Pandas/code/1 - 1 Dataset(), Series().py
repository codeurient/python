# Pandas datalarin (informasiyanin) analizi ve emali ucun istifade edilen Python kitabxanasıdır. Ferqli data tipleri, cedveller ile işləmək 
# üçün güclü alətlər təqdim edir.

# Pandas iki əsas hisseden ibaretdir: Series və DataFrame. Series birölçülü arraydir, DataFrame isə ikiölçülü verilənlər cədvəlidir.


# Pandas ile datalari import (proqrama endirmek) etmək asandır:  CSV, Excel, JSON, SQL ve müxtəlif fayl formatlarında olan məlumatları 
# import etməyə imkan verir.

# Məlumatların Təhlili və Vizualizasiyası: Pandas sizə təsviri statistikanın hesablanması, verilənlərin qruplaşdırılması, korrelyasiyaların 
# hesablanması və Matplotlib və Seaborn kimi vizuallaşdırma kitabxanaları ilə inteqrasiya vasitəsilə məlumatların vizuallaşdırılması kimi müxtəlif 
# məlumat təhlillərini həyata keçirməyə imkan verir.

# Pandas verilənlərin analitikası, suni intellekt, maliyyə, elmi tədqiqatlar, veb inkişafı və cədvəl verilənləri ilə işləməyi və təhlil 
# etməyi tələb edən digər sahələrdə geniş istifadə olunur.



import pandas as pd

# Series
s = pd.Series([10, 20, 30, 40, 50])
print(s)



# DataFrame
melumatlar = {  
                'Ad':    ['Alisa', 'Bob', 'Carli', 'Cessi'],
                'Yash':  [25, 30, 35, 40],
                'Seher': ['New-York', 'London', 'Paris', 'Tokio']
            }

df = pd.DataFrame(melumatlar)
print(df)