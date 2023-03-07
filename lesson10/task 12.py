def old(f, s):
    while f in dic:
        f = dic[f]
        if f == s:
            return True
    return False
dic = {}
for i in range(int(input())-1):
    a, b = input().split()
    dic[a] = b
for i in range(int(input())):
    a, b = input().split()
    if old(a, b):
        print(2, end=' ')
    elif old(b, a):
        print(1, end=' ')
    else:
        print(0, end=' ')
