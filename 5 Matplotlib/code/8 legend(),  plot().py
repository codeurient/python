import matplotlib.pyplot as plt

x = ['day1', 'day2', 'day3', 'day4', 'day5']
y = [300, 420, 250, 230, 400]
y1 = [500, 450, 300, 250, 320]


# Bir diaqram uzerinde iki xett yaratmaq mumkundur.
plt.plot(   x, y, marker='^',   ls="--",   color="red",   label="week1"  )
plt.plot(   x, y1, marker='*',   ls="-",   color="green",   label="week2",   alpha=0.5   )

# Diaqrammaya açıxlama mətni əlavə etmək üçün istifadə olunur. Legend hansı qrafikin hansı verilənlərə aid olduğunu müəyyən etməyə kömək edir.
# legend() funksiyası çağırıldıqda, Matplotlib avtomatik olaraq label etiketləri əsasında legend yaradır və sağ üst tərəfə yerləşdirir.
plt.legend()

plt.show()  


#! Jupyter proqraminda bu metodlarin parametrleri haqqinda etrafli acixlamalar movcuddur.