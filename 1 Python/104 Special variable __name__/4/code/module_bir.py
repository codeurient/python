
#! Neye gerekdir bu "__name__" variable -i ? Harda ne ucun istifade edeceyik ?
# Ele kod ola biler ki, hemin kod bir bawa iwe salindiqda iwlesin. Yəni, diger faylin icinde import edildikde iwlemesin.

# Meselen, kenar menbeden kod gotururk ve bu kodu yerlesdiririk awagida olan if konstruksiyasinin icine.
# Bu if konstruksiyasi wert qowur hemin kodu iwe salmaq ucun. Wert ondan ibaretdir ki, "__name__" variable-i
# beraber olmalidi "__main__" stringine ve eger beraberdirse hemin kenar menbeden elde edilen kod bu hal-hazir ki,
# senedin icinde iwlesin. 

# Yox eger biz bu fayli bawqa faylin icinde import ederek cagirsaq "__name__" beraber olmayacaq "__main__" string-ine
# ona gore de hemin kodlar iwlemeyecek.

if __name__ == '__main__':
    print("bu modul bir basa işə salinmisdir")

else:
    print("bu modul dolayi yol ile işə salinmisdir")