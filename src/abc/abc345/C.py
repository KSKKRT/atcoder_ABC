from collections import defaultdict

d = defaultdict(int)
S = input()
N = len(S)
for s in S:
    d[s] += 1
v = list(d.values())
dup = False
for n in v:
    if n >= 2:
        dup = True
        break
res = 0
if len(v) != 1:
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            res += v[i] * v[j]
if len(v) == 1 or dup:
    res += 1
print(res)
