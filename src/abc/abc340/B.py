Q = int(input())
A = []
for _ in range(Q):
    key, n = map(int, input().split())
    if key == 1:
        A.append(n)
    else:
        print(A[len(A) - n])
