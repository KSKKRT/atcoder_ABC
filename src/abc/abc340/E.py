N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(M):
    j = B[i] + 1
    balls = A[B[i]]
    A[B[i]] = 0
    while balls > 0:
        if j >= N:
            j = 0
        A[j] += 1
        balls -= 1
        j += 1
print(*A)
