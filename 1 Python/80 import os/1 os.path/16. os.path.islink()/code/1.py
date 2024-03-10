# islink() - bu metod yolun simvolik link olub olmadigini teyin edir.

# Nedir simvolik link ? OS-lerde coxlu qovluqlar ve fayllar vardir. Bu fayllar 
# cox derin qovluqlar icerisinde yerlewmiw ola bilerler ve hemin fayli acmaq ucun 
# her defe bu qeder derine enmek mecburiyyetinde qalmamaq ucun simvolik linkler yaradilir.

# Meselen: test.txt yerlewir tutaq ki, 15 dene qovlugun icinde bizde hemin eyni fayli ferqli ad
# ile simvolik link kimi yaradiriq esas ekranda ve artiq her defe 15 qovlugu acmaga ehtiyac qalmir. 

# Artiq ana ekranda olan bu fayli acdiqda eslinde esas fayli acmiw hesab edilecekdir.

# Hal-hazirda test.html link deyildir onun ucun FALSE elde edirik.


import os

faylin_yolu = '/Users/proj/domains/PYTHON/test.txt'


fayl_haqqinda = os.path.islink(faylin_yolu)

print(  fayl_haqqinda  )





# os.symlink(faylin_yolu, 'yeniFayl.txt')
