import time

# UTC formatinda olan vaxtin elde edilmesi ucun istifade edilen funksiyanin adi: #! gmtime()
localVaxt =  time.gmtime()  
print(localVaxt)

oxunaBilenFormat = time.strftime("%Y-%m-%d %H:%M:%S", localVaxt)
print(oxunaBilenFormat)