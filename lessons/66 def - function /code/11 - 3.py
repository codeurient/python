# Parametrin bawinda 2 ulduz simvolu qoyduqda bu artiq dict tipi olur. 

def seninAdinNedir(**telebe):
  
    print( "Gorkemli sairlerimiz:" )
    for acarSoz, deyer in telebe.items(): 
        print(deyer)  
     
seninAdinNedir(sair1 = "Semed Vurgun", sair2 = "Bextiyar Vahabzade", sair3 = "Nizami Gencevi")