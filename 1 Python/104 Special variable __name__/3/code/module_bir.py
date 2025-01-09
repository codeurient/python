# 1. "module_bir.py" faylinin icinde asagida gorduyunuz kodlari yazdiq.

# 2. "module_iki.py" faylinin icinde "module_bir.py" faylini import edirik.


# Sorgu ile sert qosuruq. Eger "__name__" beraberdirse "__main__" stringine, onda 'if' konstruksiyasi TRUE qaytaracaq ve 
# onun icinde olan kodlar iwleyecek. #! "__name__" variable-inin deyeri "__main__" oldugu ucun ve hal hazirda icinde oldugumuz
#! fayl-da esas fayl yəni, "__main__" sayildigi ucun biz proqrami ise saldiqda Bu if konstruksiyasi TRUE qaytarir.
if __name__ == '__main__':
    print("bu modul bir basa işə salinmisdir")

# Bu fayli basqa faylin icinde import etsek. Meselen, "module_iki.py" faylinin icinde, "module_bir.py" faylini import etsek, 
# 'if' konstruksiyasi FALSE qaytaracaq ve 'else' icinde olan kodlar isleyecekdir. 
else:
    print("bu modul dolayi yol ile işə salinmisdir")




#? Kodu 1ci burda işə salin sonra diger faylin icinde.