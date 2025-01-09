from tkinter import *
#! 3) 'event.widget'  yazaraq, asagida yaratmis oldugumuz QUTU WIDGET-ini (etiket) cagiririq. Hemin QUTU WIDGET-i kursor basildiqda cagrilir.
def surusdurmenin_baslangici(event):
    #! 5) QUTU WIDGET-ini 'vidjet' adli variable yaradaraq hemin variable-in icine qoyuruq. 
    vidjet = event.widget
    #! 6) Bu variable artiq bir OBJECT-dir. <class 'tkinter.Label'>.     'baslangicOxuX'  ise bu obyektin atributu olacaqdir.
    #!  'baslangicOxuX' - atributuna, qutunun basildigi yerin (event.x) x oxunun koordinatlarini veririk.
    #!  'baslangicOxuY' - atributuna, qutunun basildigi yerin (event.y) y oxunun koordinatlarini veririk.
    vidjet.baslangicOxuX = event.x
    vidjet.baslangicOxuY = event.y
#! 4) 'event.widget'  yazaraq, asagida yaratmis oldugumuz QUTU WIDGET-ini (etiket2) cagiririq. Hemin QUTU WIDGET-i kursor surusduruldukde cagrilir.
def surusdurmenin_hereketi(event):
    #! 7) QUTU WIDGET-ini 'vidjet' adli variable yaradaraq hemin variable-in icine qoyuruq.
    vidjet = event.widget
    #! 8) winfo_x() - bu metod QUTU WIDGET-inin pəncərənin sol kənarından ne qeder mesafede yerlesdiyini qaytarir.
    #? x = 0 (qutu widget-i pencereden 0px mesafededir) - 96 (qutu widget-ine kliklendikde elde edilen n px-i) + 97 (qutu widget-ini hereket etdirdikde n+1 px-i) = 1
    #? x = 1 (qutu widget-i pencereden 1px mesafededir) - 96 (qutu widget-ine kliklendikde elde edilen n px-i) + 97 (qutu widget-ini hereket etdirdikde n+1 px-i) = 2
    #? x = 2 (qutu widget-i pencereden 2px mesafededir) - 96 (qutu widget-ine kliklendikde elde edilen n px-i) + 97 (qutu widget-ini hereket etdirdikde n+1 px-i) = 3
    #? x = 3 (qutu widget-i pencereden 3px mesafededir) - 96 (qutu widget-ine kliklendikde elde edilen n px-i) + 97 (qutu widget-ini hereket etdirdikde n+1 px-i) = 3 ve.s
    x = vidjet.winfo_x() - vidjet.baslangicOxuX + event.x
    #! 9) winfo_y() - bu metod QUTU WIDGET-inin pəncərənin yuxari sol kənarından ne qeder mesafede yerlesdiyini qaytarir.
    #? y = 0 (qutu widget-i pencereden 0px mesafededir) - 96 (qutu widget-ine kliklendikde elde edilen n px-i) + 97 (qutu widget-ini hereket etdirdikde n+1 px-i) = 1
    #? y = 1 (qutu widget-i pencereden 1px mesafededir) - 96 (qutu widget-ine kliklendikde elde edilen n px-i) + 97 (qutu widget-ini hereket etdirdikde n+1 px-i) = 2
    #? y = 2 (qutu widget-i pencereden 2px mesafededir) - 96 (qutu widget-ine kliklendikde elde edilen n px-i) + 97 (qutu widget-ini hereket etdirdikde n+1 px-i) = 3
    #? y = 3 (qutu widget-i pencereden 3px mesafededir) - 96 (qutu widget-ine kliklendikde elde edilen n px-i) + 97 (qutu widget-ini hereket etdirdikde n+1 px-i) = 3 ve.s
    y = vidjet.winfo_y() - vidjet.baslangicOxuY + event.y
    vidjet.place(x = x, y = y) #! 10) test ucun x ve y oxlarina ededleri manual olaraq verib yoxlamaq olar.

pencere = Tk()
#! 1) Label() klasi ile qutu WIDGET-i yaradiriq ve place() metodu ile hemin qutu WIDGET-ini 'pencere'-ye yerlesdiririk.
etiket = Label(pencere, bg="red", width=10, height=5)
etiket.place(x=0, y=0)
etiket2 = Label(pencere, bg="blue", width=10, height=5)
etiket2.place(x=100, y=100)

#! 2) bind() metodu ile EVENT (hadise) yaradiriq. Hemin hadise qutunu klikledikde, 'surusdurmenin_baslangici' adli funksiyamiz işə dusur.
#! Diger EVENT (hadise) ise, qutunu surusdurdukde hadisesidir ve qutunu surusdurdukde 'surusdurmenin_hereketi' adli funksiyamiz işə dusur.
etiket.bind("<Button-1>",  surusdurmenin_baslangici)
etiket.bind("<B1-Motion>", surusdurmenin_hereketi)
etiket2.bind("<Button-1>",  surusdurmenin_baslangici)
etiket2.bind("<B1-Motion>", surusdurmenin_hereketi)
pencere.mainloop()  









