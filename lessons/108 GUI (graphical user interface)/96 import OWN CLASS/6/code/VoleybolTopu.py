class VoleybolTopu:

    def __init__(self, canvas, x, y, diametr, xOxununSureti, yOxununSureti, reng):
        self.canvasDeyiskeni = canvas
        self.sekil    = canvas.create_oval(x, y, diametr, diametr, fill=reng)  
        self.xSureti  = xOxununSureti
        self.ySureti  = yOxununSureti
    
    def hereket(self):
        koordinatlar = self.canvasDeyiskeni.coords(self.sekil)
        print(koordinatlar) 

        if( koordinatlar[2] >= self.canvasDeyiskeni.winfo_width() or koordinatlar[0] < 0 ):
            self.xSureti = -self.xSureti
        if( koordinatlar[3] >= self.canvasDeyiskeni.winfo_height() or koordinatlar[1] < 0 ):
            self.ySureti = -self.ySureti

        self.canvasDeyiskeni.move(self.sekil, self.xSureti, self.ySureti) 