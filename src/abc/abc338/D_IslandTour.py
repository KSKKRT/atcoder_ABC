N, M = map(int, input().split())
X = list(map(int, input().split()))

ans = [0 for _ in range(N + 1)]
for i in range(M - 1):
    s, e = X[i], X[i + 1]
    if s > e:
        s, e = e, s

    d = e - s
    ans[s] += N - d
    ans[e] -= N - d
    ans[0] += d
    ans[s] -= d
    ans[e] += d
    ans[N] -= d

for i in range(N):
    ans[i + 1] += ans[i]

print(min(ans[:-1]))
