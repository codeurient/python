# replace() - funksiyası DataFrame-də müəyyən dəyərləri başqa bir dəyərlə əvəz etmək üçün istifadə olunur.

# 1ci parametrde NumPy kitabxanasinin 'nan' kodundan istifade edirik.
# 2ci parametrde bos xanalar ne ile evez edilecek onu yaziriq.


import pandas as pd
import numpy as np

melumatlar = pd.read_csv('Datasets-main/company1.csv')


# Burda deyeri NaN olan xanalari 'Hello' sozu ile evez edirik.
print(melumatlar.replace(np.nan, 'Hello')) 