# dict icindeki her hansisa bir acar sozu silmek ucun pop() metodundan istifade edilir.

# pop() metodu icinde silinmesi lazim olan acar sozu string tipinde yazmaliyiq

melumatlar = {
  "istehsalatci": "Renault",
  "model": "Clio",
  "il": 2009
}

melumatlar.pop("il")

print(melumatlar)