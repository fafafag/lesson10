def predki(deti, kek):
    z = []
    z.append(deti)
    while deti in kek:
        deti = kek[deti]
        z.append(deti)
    return z
kek = dict()
for i in range(int(input()) - 1):
    deti, j = input().split()
    kek[deti] = j
for i in range(int(input())):
    deti1, deti2 = input().split()
    prapra = set(predki(deti1, kek))
    for t in predki(deti2, kek):
        if t in prapra:
            print(t)
            break
