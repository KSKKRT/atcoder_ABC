def has_substring(W, B):
    # 基本パターン
    pattern = "wbwbwwbwbwbw"
    repeated_pattern = pattern * 100
    N = len(repeated_pattern)
    # 累積カウンターを初期化
    w_count = [0 for _ in range(N + 1)]
    b_count = [0 for _ in range(N + 1)]

    # スライディングウィンドウで累積カウントを更新
    for i in range(N):
        if repeated_pattern[i] == "w":
            w_count[i + 1] = w_count[i] + 1
            b_count[i + 1] = b_count[i]
        else:
            w_count[i + 1] = w_count[i]
            b_count[i + 1] = b_count[i] + 1

    for i in range(N):
        for j in range(i + 1, N + 1):
            w = w_count[j] - w_count[i]
            b = b_count[j] - b_count[i]
            if w == W and b == B:
                return True
    return False


W, B = map(int, input().split())
print("Yes" if has_substring(W, B) else "No")
