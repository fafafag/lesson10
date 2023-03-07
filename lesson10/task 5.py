n = int(input())
x = {'write': 'W', 'read': 'R', 'execute': 'X'}
d = {}
for i in range(n):
    a, *b = input().split()
    d[a] = set(b)
for i in range(int(input())):
    a, b = input().split()
    if x[a] in d[b]:
        print('OK')
    else:
        print('Access denied')
