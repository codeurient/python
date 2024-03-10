# mueyyen edilmis faylin yaxud qovlugun ne derece el catan olub olmadigini yoxlayir.

# Mesel ucun bezi fayllar yaxud qovluqlar vardir ki, hemin fayllarin icine yazi ve.s yazmaq olmur.
# Yaxud bezi fayllar yaxud qovluqlar vardir ki, onlari açıb icine baxmaq olmur ve.s

# Bu access() metodu da yoxlayir ki, hemin mueyyen fayl yaxud qovluq ne qeder el catandir 
# bizim ucun. Icine daxil ola bilerikmi yaxud icine yazi yaza bilerikmi yaxud umumiyyetle
# bele bir fayl movcuddurmu.

# Bu metodun 2 mutleq yazilmasi gerek parametri vardir. 1cisi fayl yaxud qovlugun yolu.
# 2cisi ise mod yeni rejim. Rejimler ise 4 denedir. 

# os.F_OK - movcudlugu yoxlayir
# os.R_OK - fayli yaxud qovlugu acib icindekileri oxumaq olurmu deye yoxlayir
# os.W_OK - fayli yaxud qovlugu acib icine nese yazmaq, qoymaq olurmu deye yoxlayir

# os.X_OK - fayli işlətməyə icazənin olub olmadığıni yoxlayır. Yeni, bu fayl istenilen formada 
# ola biler. Meselen, bir fayl var ve icinde kod var. Bu kod tesevvur edin ki, virusdu ve
# hemin fayli istenilen adam işə salaraq ziyan vura biler. Normal halda buna icaze yoxdur.
# Buna gore de os.W_OK false olaraq geri qayidir. Yeni kenardan mudaxile ederek fayliişə salmaq olmur. 

import os

yol = '/Users/proj/domains/PYTHON/main.py'

melumat = os.access(yol, os.X_OK)

print(melumat)