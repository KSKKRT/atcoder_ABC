N = int(input())
humans = [[-1, -1] for _ in range(N)]
order = list(map(int, input().split()))
for i in range(N):
    if order[i] == -1:
        cur = i
        continue
    humans[i][0] = order[i]
    humans[order[i] - 1][1] = i
res = []
while True:
    res.append(cur + 1)
    cur = humans[cur][1]
    if cur == -1:
        break
print(*res)
