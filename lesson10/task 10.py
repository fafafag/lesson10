from collections import defaultdict
A = defaultdict(dict)
while True:
    try: s, j, i = input().split()
    except: break
    A[s][j] = A[s].get(j, 0)+int(i)
for i, j in sorted(A.items()):
    print(i+':')
    for sub, count in sorted(j.items()):
        print(sub, count)