slovar = {}
a = int(input())
for i in range(a):
    first, second = input().split()
    slovar[first] = second
    slovar[second] = first
print(slovar[input()])