# loads() - STRING formatinda daxil olan melumatlari, bize lazim olan ve istifade ede bileceyimiz dict formatina geri
# cevirmek ucun bu metodan istifade edilir.     #! deserialization

import json

telebe_melumatlari = """{"ad": "Kamal", "yash": 16, "bal": 655}"""



melumat = json.loads(telebe_melumatlari)
print(type(melumat))
print(   melumat['ad']  )