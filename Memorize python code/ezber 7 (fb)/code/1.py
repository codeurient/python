m = [7, 2, -5, 1, 1, -1, 5, -5]
k = 5

cnt = 0

for x in range(len(m)-1):
    for y in range(x, len(m)):
        if sum(m[x:y+1]) == k:
            print(m[x:y+1])
            cnt += 1

print(cnt)