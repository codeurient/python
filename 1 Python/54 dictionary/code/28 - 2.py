import json

telebe_melumatlari = {"ad": "Kamal", "yash": 16, "bal": 655}

# dumps() metodunun:
    # 1ci parametri                                 - string formatina cevrilecek dict 
    # 2ci parametri indent=10                       - her melumat yeni setrden baslasin ve 10 simvol ara boslugu ile yazilsin
    # 3ci parametri separators=(',',    '=')        - melumatlar vergul ve beraberlik simvollari ile ayrilsin bir-birinden
melumat = json.dumps(telebe_melumatlari, indent=2, separators=(',',     '='))
print(  melumat  )