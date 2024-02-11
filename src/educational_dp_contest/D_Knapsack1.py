N, W = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
for n in range(1, N + 1):
    for w in range(W + 1):
        if w - items[n - 1][0] >= 0:
            dp[n][w] = max(dp[n][w], dp[n - 1][w - items[n - 1][0]] + items[n - 1][1])
        dp[n][w] = max(dp[n][w], dp[n - 1][w])
print(dp[-1][-1])
