# relplot() funksiyasi 2 sutun arasındakı əlaqəni diaqram ile ifade etmek üçün istifadə olunur. Bu funksiya default olaraq noqte qrafikasindan
# istifade edir. Bu funksiyadan nöqtə qrafikləri, xətt qrafikləri və ya digər növ vizualizasiyaları yaratmaq üçün istifadə edilə bilər.

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
print(data)

# sns.relplot(data = data, x = "tip", y = "total_bill", hue="sex", kind="scatter")
# sns.relplot(data = data, x = "tip", y = "total_bill", hue="sex", kind="line")
sns.relplot(data = data, x = "tip", y = "total_bill", hue="sex", col="day")

plt.show()