class VoleybolTopu:

    def __init__(self, canvas, x, y, diametr, xOxununSureti, yOxununSureti, reng):
        self.canvasDeyiskeni = canvas
        self.sekil    = canvas.create_oval(x, y, diametr, diametr, fill=reng)  
        self.xSureti  = xOxununSureti # 1
        self.ySureti  = yOxununSureti # 1

    def hereket(self):
        koordinatlar = self.canvasDeyiskeni.coords(self.sekil)
        print(koordinatlar)

        #! 1.
        # Canvas() klasinin move() metodu ile sekli hereket etdiririk. 
        # move() metodunun 1ci parametri (self.sekil)   - herket etdirilecek sekildir.
        # move() metodunun 2ci parametri (self.xSureti) - seklin X oxu uzre herket edeceyi koordinatdir. +1
        # move() metodunun 3ci parametri (self.ySureti) - seklin Y oxu uzre herket edeceyi koordinatdir. +1
        self.canvasDeyiskeni.move(self.sekil, self.xSureti, self.ySureti) 