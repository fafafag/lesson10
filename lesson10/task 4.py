n = int(input())
a = {}
for j in range(n):
    for i in input().split():
        a[i] = a.get(i, 0) + 1
mx = 0
ma = ''
for i in sorted(a):
    if a[i] > mx:
        ma = i
        mx = a[i]
print(ma)
