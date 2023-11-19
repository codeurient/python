# eger yenede tuple-in deyerini deyismek isteyirsinizse onda ilk once bu tuple-i
# list-e cevirmek lazimdir sonra ise geri tuple-a


telebe = ("Aleks", 21, "male", "green", "baku")   

siyahi = list(telebe)
siyahi[0] = 'Bob'

yeniTelebe = tuple(siyahi)

print(    yeniTelebe    )