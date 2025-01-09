from tkinter import *
    
def goruntulemek():
    # 4) 'x' adlı variable-in aldigi deyeri get() metodu ile elde ederek if ile şərt qoşuruq.
    if(x.get() == 1):
        print("Raziliq verdin")
    else:
        print("Imtina etdin")





pencere = Tk()

# 2) IntVar() tkinter modulunun klasidir. 'x' adlı variable-a verəcəyimiz dəyərin tam ədəd olması üçün istifade edirik.
# 1) Burda ilk öncə 'x' adlı variable yaradılır sonra isə həmin variable Checkbutton() klasına verilir.
x = IntVar()

# 3) Proqramı işə saldıqda XANA seçili olmur. Xananı biz özümüz seçdikdə 'x' adlı variable-a 1 ötürülür. 
# xananı seçmədikdə isə 'x' adlı variable-a 0 ötürülür. Həmin 1 və 0 dəyərlərini 'x' adlı variable-a ötürmək üçün
# onvalue=1 və offvalue=0 parametrlərindən istifadə edirik.
#? onvalue=1     - x variable-inin deyerini aktiv olaraq teyin edir.
#? offvalue=0    - x variable-inin deyerini inaktiv olaraq teyin edir.
xana = Checkbutton( pencere, 
                    text="Men bununla raziyam", 
                    variable=x,
                    onvalue=1,
                    offvalue=0,
                    command=goruntulemek
                )

xana.pack()

pencere.mainloop()