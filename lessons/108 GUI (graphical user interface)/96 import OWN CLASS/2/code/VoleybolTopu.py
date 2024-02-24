class VoleybolTopu:

    def __init__(self, canvas, x, y, diametr, xOxununSureti, yOxununSureti, reng):
        self.canvasDeyiskeni = canvas
        self.sekil    = canvas.create_oval(x, y, diametr, diametr, fill=reng)  
        self.xSureti  = xOxununSureti
        self.xySureti = yOxununSureti

    #! 1
    # herket() adli metod yaradiriq.    
    def hereket(self):
        #! 2
        # self.canvasDeyiskeni cagririq ve coords() metodu ile SEKLIN koordinatlarini elde edirik.
        # Bu koordinatlar beledir:
            # a) x1   - Bu, yumru dairenin yuxarı sol küncünün x koordinatıdır.
            # b) y2   - Bu, yumru dairenin yuxarı sol küncünün y koordinatıdır.
            # c) x2   - Bu, yumru dairenin aşağı sağ küncünün x koordinatıdır. 
            # d) y2   - Bu, yumru dairenin aşağı sağ küncünün y koordinatıdır. 
        
            # Yuxari sol küncün x koordinatindan asagi sag küncün x koordinatina 100 px -lik bir olcu vardir. Hemcinin,
            # Yuxari sol küncün y koordinatindan asagi sag küncün y koordinatina 100 px -lik bir olcu vardir. Belelikle OVAL formalasir.
        koordinatlar = self.canvasDeyiskeni.coords(self.sekil)
        print(koordinatlar)