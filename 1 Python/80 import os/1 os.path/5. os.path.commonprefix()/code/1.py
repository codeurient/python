# commonprefix() - meselen, fayllar var ve bu fayllar heresi bir qovluqda yerlesir. 
# Hemin fayllarin hamisi ferqli qovluqlarda yerlewsede butun bu qovluqlarda esas 1 ana qovlugun 
# icerisindedir. Bu metodda hemin fayllarin ortaq yerlewmiw oldugu ana qovlugun adini qaytarir.

import os

yol = [
     "/Users/qovluq1/qovluq2/qovlu3/qovluq4/qovluq5/test1.txt",
     "/Users/qovluq1/qovluq2/test2.txt",
     "/Users/qovluq1/qovluq2/qovlu3/qovluq4/test3.txt",
     "/Users/qovluq1/qovluq2/qovlu3/test4.txt",
     "/Users/numune1/numune2/numune3/test5.txt",
     "/Users/numune1/numune2/test6.txt",
]

print(   os.path.commonprefix(yol)   )