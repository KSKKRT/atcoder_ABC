S = input()


def is_extended_abc(S: str) -> bool:
    if len(S) <= 1:
        return True
    checker = "A" * 100 + "B" * 100 + "C" * 100
    dp = [[0 for i in range(len(S) + 1)] for j in range(len(checker) + 1)]  # 0で初期化
    for i in range(len(checker)):
        for j in range(len(S)):
            if S[j] == checker[i]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return len(S) == dp[-1][-1]


print("Yes" if is_extended_abc(S) else "No")
