# spesifikator :.2f

# bu spesifikator ededlere tetbiq edilir.

# ededleri noqteden sonra nece sifir suruwdurmek lazim oldugunu teyin edir.

ad = 3.14159

print("PI ededinin qiymeti {:.2f}-dur".format(ad))          # bele de yazmaq olar
print("PI ededinin qiymeti {0:.2f}-dur".format(ad))         # bele de yazmaq olar
print("PI ededinin qiymeti {0:{1}}-dur".format(ad, '.2f'))  # bele de yazmaq olar