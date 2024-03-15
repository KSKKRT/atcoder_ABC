N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

nums = []
for i in range(N):
    for j in range(M):
        for k in range(L):
            nums.append(A[i] + B[j] + C[k])
nums = sorted(list(set(nums)))
lim = len(nums)


def binary_search(numbers, value) -> bool:
    # 探索する範囲の左端点のインデックス
    left = 0
    # 探索する範囲の右端点のインデックス
    right = len(numbers) - 1

    while left <= right:
        # 探索する範囲の中央のインデックスを計算する
        mid = (left + right) // 2

        # 探索する値が、中央のインデックスの値より小さい場合
        if value < numbers[mid]:
            # 探索する範囲を、中央のインデックスより左側に絞り込む
            right = mid - 1
        # 探索する値が、中央のインデックスの値より大きい場合
        elif value > numbers[mid]:
            # 探索する範囲を、中央のインデックスより右側に絞り込む
            left = mid + 1
        # 探索する値が、中央のインデックスの値と等しい場合
        else:
            # 探索した値を返す
            return True

    # 探索する値が見つからなかった場合は、Noneを返す
    return False


for x in X:
    if binary_search(nums, x):
        print("Yes")
    else:
        print("No")
