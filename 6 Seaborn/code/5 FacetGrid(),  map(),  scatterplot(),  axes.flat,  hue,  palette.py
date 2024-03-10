# FacetGrid() obyekti, çoxlu sub qrafikler yaratmaq üçün istifadə olunur.

# map() - FacetGrid və ya PairGrid kimi əvvəlcədən təyin edilmiş grid obyektləri ilə istifadə olunur.
# Bu funksiya teyin edilmis diaqramin her alt qrafik uzerinde ayri-ayri goruntulenmesi ucun istifade edilir.

# scatterplot() funksiyasi ədədi dəyərləri ehtiva edən iki variable arasındakı əlaqəni vizuallaşdırmaq üçün
# istifade edilir. Vizaul olaraq 2 variable arasinda ki, ferqi noqteler ile gorereik.

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
print(data)

# 1) hue parametri, sütunu secmek ve noqteleri renglemek ucun istifade edilir. 
# 2) palette={} parametri ile Male ucun blue Female ucun pink renglerini elave edirik. Bes Cedvele baxan hardan bilecek ki, Blue renk Male-dir? 
# 3) Bunun ucun diaqramin uzerine etiket elave edirik. Diaqram 2 dene oldugu ucun for dongusunden istifade edirik. 
a = sns.FacetGrid(data, col="time", height=4, hue='sex', palette={"Male": "blue", "Female": "pink"})

# 2 ci ve 3cu parametrler sutunlarindan adlarindan goturulur. Hemin sutunda olan deyerler diaqramda eks olunur.
a.map(  sns.scatterplot,  "day",  "size"  )

# 3) axes.flat kodu FacetGrid oyektinin her bir sub qrafikini elde etmek ucun istifade edilir. Elde edilen sub qrafikler 'ax' adli variable-a 
# gonderilir. Sonra legend() funksiyasi ile Hemin cinsiyyet sutunu ucun basliq metn elave edirik. Niye cinsiyyet sutunu ucun ? Cunki 'hue'
# parametrinde hemin sütunun adını qeyd etmişik. 'sex'
for ax in a.axes.flat:
    ax.legend(title="Sex")

plt.show()