# boxplot() funksiyasi, DataFrame-dəki rəqəmli verilənlərə əsasən, sütunun qutu diaqramasını çəkir.

# Qutu, verilenlerin kvartallararası diapazonunu (IQR) təmsil edir. Qutunun aşağı rübü (Q1) və yuxarı rübü (Q3) arasındakı uzunluq 
# IQR-dir. Beləliklə, bu qutu məlumatların orta 50%-ni əhatə edir. Qutunun ortasındakı xətt median dəyəri (Q2) göstərir.


# Whiskers yəni, biglar Q1 ve Q3 deyerleridir.

# Kenar Degerler (Outliers): Whiskers-in xaricinde qalan deyerlerdir.

import matplotlib.pyplot as plt
import pandas as pd

a = [25, 46, 57, 25, 45, 13, 29, 39, 46, 99, 22, 12, 14, 16, 55, 6, 46, 52, 55, 7]
series_a = pd.Series(a)
print(series_a.describe())

plt.boxplot(  a  )
plt.show()