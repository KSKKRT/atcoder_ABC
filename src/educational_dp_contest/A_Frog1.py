N = int(input())
h = list(map(int, input().split()))
inf = 10**10
dp = [inf for _ in range(N)]
dp[0] = 0

for i in range(1, N):
    if dp[i] > dp[i - 1] + abs(h[i] - h[i - 1]):
        dp[i] = dp[i - 1] + abs(h[i] - h[i - 1])
    if i > 1 and dp[i] > dp[i - 2] + abs(h[i] - h[i - 2]):
        dp[i] = dp[i - 2] + abs(h[i] - h[i - 2])
print(dp[-1])
