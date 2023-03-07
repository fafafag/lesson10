golosovanie = {}
n = input()
for i in range(int(n)):
    candidate, votes = input().split()
    golosovanie[candidate] = golosovanie.get(candidate, 0) + int(votes)
for candidate, votes in sorted(golosovanie.items()):
    print(candidate, votes)
