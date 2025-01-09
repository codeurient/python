from tkinter import *

pencere = Tk()

# 1) Menu() - bu klas, Ana ekranda menyu paneli yaradir. #! Bu 'menyu paneli' dediyimiz sey: erazi, sahe, teritoriya kimi bir seydir. 
#! Yeni erazini formalasdiririq sonra icine bir seyler elave edirik. 
menuBar = Menu(pencere)
# 2) menu= - bu parametr, yaratmis oldugumuz menyu panelini, Ana ekrana qurasdirmaq ucun istifade edilir.
pencere.config(menu=menuBar)

# 3) Menu() - hemin klasi yeniden istifade ederek 1ci parametrinde yuxarida yaratmis oldugumuz 'Menu()' klasini veririk.
# Yeni 1ci menyu paneli icinde basqa bir menyu paneli yaradiriq. 
# 4) tearoff=0 - bu parametr, menu panelindeki elave boslugu yox etmek ucundur.
fileMenu = Menu(menuBar, tearoff=0)
# 5) add_cascade() - bu metoddan istifade ederek, '1ci Menu Panelinin' icine '2ci Menu Panelini' elave edirik.
# 6) add_cascade() metodunun 'label=' parametri hemin '2ci Menu Panelinin' nece adlanacagini teyin edir.
menuBar.add_cascade(label="File", menu=fileMenu)

# 7) 2ci Menu Panelinin icine ise, 3 dene etiket elave edirik. 
fileMenu.add_cascade(label="Ac")
fileMenu.add_cascade(label="Yadda saxla")
fileMenu.add_cascade(label="Cix")

pencere.mainloop()  