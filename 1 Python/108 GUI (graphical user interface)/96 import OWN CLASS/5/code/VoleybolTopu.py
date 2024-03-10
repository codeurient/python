class VoleybolTopu:

    def __init__(self, canvas, x, y, diametr, xOxununSureti, yOxununSureti, reng):
        self.canvasDeyiskeni = canvas
        self.sekil    = canvas.create_oval(x, y, diametr, diametr, fill=reng)  
        self.xSureti  = xOxununSureti
        self.ySureti  = yOxununSureti
    
    def hereket(self):
        # 0-ci indeks - x1  - Bu, yumru dairenin yuxarı sol küncünün x koordinatıdır.
        # 1-ci indeks - y2  - Bu, yumru dairenin yuxarı sol küncünün y koordinatıdır.
        # 2-ci indeks - x2  - Bu, yumru dairenin aşağı sağ küncünün x koordinatıdır. 
        # 3-ci indeks - y2  - Bu, yumru dairenin aşağı sağ küncünün y koordinatıdır. 

        # Yuxari sol küncün x koordinatindan asagi sag küncün x koordinatina 100 px -lik bir olcu vardir. Hemcinin,
        # Yuxari sol küncün y koordinatindan asagi sag küncün y koordinatina 100 px -lik bir olcu vardir. Belelikle OVAL formalasir.
        koordinatlar = self.canvasDeyiskeni.coords(self.sekil)
        print(koordinatlar) 

        # koordinatlar[0] - x1 oxunun koordinatini elde edirik. 
        # move() metodu vasitesi ile, x1 ve y1 oxlarinin deyerleri yavas-yavas artacaqdir. 
        # x1 ve y1 artigi zaman avtomatik olaraq x2 ve y2 de artacaqdir. 
        #! x1 - koordinatlar[0] -dir
        #! y1 - koordinatlar[1] -dir
        #! x2 - koordinatlar[2] -dir
        #! y2 - koordinatlar[3] -dur
        # x2 ve y2 oxlari yeni 100 arta-arta gelib 506-ya beraber olduqda artan deyerler azalmaga baslasin demisik.     1  =  -1  =  -1  
        # x1 ve y1 oxlari yeni 0 azala-azala gelib -1-e beraber olduqda azalan deyerler artmaga baslasin demisik.      -1  =  -1  =   1    
        if( koordinatlar[2] >= self.canvasDeyiskeni.winfo_width() or koordinatlar[0] < 0 ):
            self.xSureti = -self.xSureti
        if( koordinatlar[3] >= self.canvasDeyiskeni.winfo_height() or koordinatlar[1] < 0 ):
            self.ySureti = -self.ySureti

        self.canvasDeyiskeni.move(self.sekil, self.xSureti, self.ySureti) 