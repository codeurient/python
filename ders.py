siyahi1 = [20, 30, 40, 50, 60, 70]
siyahi2 = []





for i in siyahi1:
    if i > 45:
        siyahi2.append(i)
print(siyahi2)





siyahi3 = [  i         for i in siyahi1        if i > 45    ]
print(siyahi3)