# parametr-e 1 ulduz simvolu vermeyi kecdik. 1 ulduz ne vaxt verilirdi ? 
# Eger nece parametr yaratmaq lazim oldugunu bilmedikde dedik. Ve istenilen qeder deyer vermek mumkundur dedik.

# hemin parametrin evvelinde 2 ulduz simvoluda yazmaq mumkundur. Bes bu ne menaya gelir ?
# funksiyani cagiran zaman sadece deyerler gonderirdik? Eger hem "acar soz" hemde "deyer" eyni vaxtda gondermek
# isteyirikse, onda 1 parametrin evvelinde 2 ulduz simvolu yazmaq lazimdir.

def seninAdinNedir(**telebe):
  
    print( "Meshur sair " + telebe["ad"] + " " + telebe["soyad"] )
     
seninAdinNedir(ad = "Semed", soyad = "Vurgun")