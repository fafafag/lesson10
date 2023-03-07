slovar = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        slovar[city] = country

for i in range(int(input())):
    print(slovar[input()])