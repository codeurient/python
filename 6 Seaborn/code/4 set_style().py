# set_style() funksiyasi, qrafiklere daha ferqlistiller elave etmek ucun istifade edilir.
    
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import seaborn as sns
import matplotlib.pyplot as plt


data = sns.load_dataset("exercise")
print(data)

sns.set_style(style="dark")
sns.barplot(x='time',  y='pulse',  data=data)
plt.show()