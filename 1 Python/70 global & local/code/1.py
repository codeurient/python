# GLOBAL ve LOCAL variable-llar (deyiskenler)

# 1. local deysikenler cari funksiya icinde istifade edilen deyiskenlere deyilir ve
# sadece yaratmiw oldugumuz cari funksiyanin icinde istifade etmek mumkundur.

# 2. global deyiskenler funksiyanin xaricinde istifade edilen deyiskenlere deyilir ve 
# proqram kodunun istenilen yerinde istifade etmek mumkundur.

# Eyni adda global ve local deyisken yaratdiqda bu deyiskenler adlari eyni olsa bele, 
# ferqli deyiskenler sayilacaqdir.

ad = "Ali" # GLOBAL variable

def cari_funksiya():
    ad = "Jony" # LOCAL variable
    print(ad)
    
cari_funksiya()

print(ad)



