# movcud olan deyeri deyisdirmek ucunde 'acar sozden' istifade etmek olar ancaq get() metodundan istifade 
# etmek olmaz. 


melumatlar = {
  "istehsalatci": "Renault",
  "model": "Clio",
  "il": 2009
}

melumatlar['il'] = 2010

deyer = melumatlar['il']

print(deyer)