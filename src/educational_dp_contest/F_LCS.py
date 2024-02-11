s = input()
t = input()
N, M = len(s), len(t)
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

i, j = N, M
inv_result = []
while i > 0 and j > 0:
    while j > 1 and dp[i][j] == dp[i][j - 1]:
        j -= 1
    while i > 1 and dp[i][j] == dp[i - 1][j]:
        i -= 1
    if s[i - 1] == t[j - 1]:
        inv_result.append(s[i - 1])
    i -= 1
    j -= 1

print("".join(inv_result[::-1]))
