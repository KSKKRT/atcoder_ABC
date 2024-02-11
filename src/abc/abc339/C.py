N = int(input())
A = list(map(int, input().split()))

cum = [A[0]]
for i in range(1, N):
    cum.append(cum[i - 1] + A[i])
lim = min(cum)
cum_all = sum(A)
print(cum_all if lim > 0 else cum_all - lim)
