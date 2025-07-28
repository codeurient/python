# lambda funksiyani def funksiyasinin icinde yazmisiq. 

# numune() adli funksiyamizi cagirdiqda proqram avtomatik olaraq lamba funksiyani gorur ve
# hemin lambda funksiyani iwe salir birinci. 

# numune(2) funksiyasini vurma adinda olan variable-a veririk ve vurma(11) dedikde lambda funksiyasini cagirmis oluruq

# Yeni, numune(2)-nin verildiyi vurma variable-i eslinde artiq lambda funksiyadir ve bu lambda 
# funksiyanin a parametri 11 deyerine sahibdir. vurma(11) dedikde biz lambda funksiyani cagirmis oluruq.

# 11 deyeri a parametrine verilir ve lambda funksiyasi a -ni n-e vurur. 2 * 11 = 22.

def numune(n):
  return lambda a : a * n

vurma = numune(2)

print(    vurma(11)    )




