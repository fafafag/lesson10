Capitals = {}
for i in input().split():
     Capitals[i] = Capitals.get(i, 0) + 1
     print(Capitals[i] - 1, end=' ')
