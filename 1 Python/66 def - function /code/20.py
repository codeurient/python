# rekursiv(k - 1) yazdigimiz yere 1 defe 7 deyeri qoyularaq hesablama aparilir. 

# rekursiv(7 - 1) = 6 edir ve hemin bu 6 ededi kenara qeyd olunur ki, sonra istifade edilsin. Bu 6 ededinin istifade edilmeye 
# baslanmasi ucun 7 ededi ile bawlamiw hesablama bitmelidir, tamamlanmalidir.

# 7 ededi ile bawlayan hesablama bitdikden sonra 6 hesablanir ve rekursiv(6 - 1) = 5 ededi kenara yaddawa qeyd edilir.
# 6 ededi ile olan hesablama bawa catdiqdan sonra 5 ededi ile olan hesablama iwe kecir ve.s 


# 7 + rekursiv(7 - 1) + rekursiv(6 - 1) + rekursiv(5 - 1) + rekursiv(4 - 1) + rekursiv(3 - 1) + rekursiv(2 - 1) + rekursiv(1 - 1)   = 28


# 6 + rekursiv(6 - 1) + rekursiv(5 - 1) + rekursiv(4 - 1) + rekursiv(3 - 1) + rekursiv(2 - 1) + rekursiv(1 - 1)                     = 21


# 5 + rekursiv(5 - 1) + rekursiv(4 - 1) + rekursiv(3 - 1) + rekursiv(2 - 1) + rekursiv(1 - 1)                                       = 15


# 4 + rekursiv(4 - 1) + rekursiv(3 - 1) + rekursiv(2 - 1) + rekursiv(1 - 1)                                                         = 10


# 3 + rekursiv(3 - 1) + rekursiv(2 - 1) + rekursiv(1 - 1)                                                                           = 6


# 2 + rekursiv(2 - 1) + rekursiv(1 - 1)                                                                                             = 3


# 1 + rekursiv(1 - 1)                                                                                                               = 1

def rekursiv(k):
  
  if(k > 0):
    netice = k + rekursiv(k - 1)
    print(netice)

  else:
    netice = 0
  return netice

rekursiv(7)