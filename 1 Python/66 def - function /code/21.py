# faktorialin hesablanmasi.

# Ilk once 1 defe faktoriyel(4) funksiyasi cagrilir ve n parametrine 4 ededi verilir.

# Sonra ise faktoriyel(n-1) oz icinde yeniden tekrar tekrar cagrilir ta ki, n == 1 olana qeder
# faktoriyel(4-1) = 3
# faktoriyel(3-1) = 2
# faktoriyel(2-1) = 1

# Ve here defe yeni deyer emele gelir ve bu yeni deyer n parametrine yeniden gonderilir ve 
# if sorgusunun icinde 1 == 1 olduqda funksiya return edir n parametini. Bu n parametri en sonunda 1 ededidir.

# Ancaq 1 olana qeder 4 == 1 false verir ve else kodu iwleyir, 
#                     3 == 1 false verir ve else kodu iwleyir, 
#                     2 == 1 false verir ve else kodu iwleyir, 
#                     1 == 1 true  verir ve if   kodu iwleyir, 

# Her else kodu isledikde hesablama bu sekilde aparilir:
# 4 * faktoriyel(4-1) * faktoriyel(3-1) = 24 cavabini aliriq.


def faktoriyel(n):  
   if n == 1:  
       return n  
   else:  
       return n*faktoriyel(n-1)  

print(   faktoriyel(10)   )

























