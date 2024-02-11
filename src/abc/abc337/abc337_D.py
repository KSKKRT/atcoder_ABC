def min_operations(grid, H, W, K):
    row_operations = 0
    col_operations = 0

    # 各行において操作が必要かどうかを確認
    for i in range(H):
        count = grid[i].count('.')
        if count < K and row_operations > K - count:
            row_operations = K - count

    # 各列において操作が必要かどうかを確認
    for j in range(W):
        count = sum(grid[i][j] == '+' for i in range(H))
        if count < K:
            col_operations += K - count

    # 最小の操作回数を出力
    return min(row_operations, col_operations)
