s_eq, s_all = set(), set()
for i in range(int(input())):
    s = input()
    s_eq.add(s)
    s_all.add(s.lower())
print(sum([1 for s in input().split()
if not s in s_eq
and (s.lower() in s_all
or s not in [s.lower()[:i] + s.lower()[i: i+1].upper() + s.lower()[i+1: len(s)]
for i in range(len(s))])]))
