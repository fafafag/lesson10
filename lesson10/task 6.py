slov = {}
for i in range(int(input())):
    str = input().split()
    for j in str:
        slov[j] = slov.get(j, 0) + 1
for j in sorted(slov.items(), key = lambda x: (-x[1], x[0])):
    print(j[0])
