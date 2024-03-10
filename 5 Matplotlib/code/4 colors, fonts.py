import matplotlib.pyplot as plt

y = [98, 67, 88, 95, 88, 100]
x = ['Part1', 'Part2', 'Part3', 'Part4', 'Part5', 'Part6']
colors = ['red', 'green', 'yellow', 'blue', 'orange', 'purple']

plt.bar(x, y, color=colors, edgecolor='black')
# plt.bar(x, y, color='red') - bu cur yazaraqda diaqrama reng vermek olar.
# yaxud list yaradaraq deyerleri variable vasitesi ile de gondermek olar.


#  fontsize=17 yazaraq yazilarin olcusunu boyutmek mumkundur.
plt.xlabel("Parts of Movie", fontsize=17)
plt.ylabel("Populatity", fontsize=17)
plt.title("Populatity of Different parts of Movie", fontsize=17)

plt.show()