N, K = map(int, input().split())
h = list(map(int, input().split()))
inf = 10**10
dp = [inf for _ in range(N)]
dp[0] = 0

for i in range(N - 1):
    end = min(i + K, N - 1) + 1
    for j in range(i + 1, end):
        dp[j] = min(dp[j], dp[i] + abs(h[i] - h[j]))
print(dp[-1])
