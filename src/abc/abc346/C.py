N, K = map(int, input().split())
A = list(map(int, input().split()))
cand_A = []
for i in range(len(A)):
    if A[i] > K:
        continue
    cand_A.append(A[i])
cand_A = list(set(cand_A))

print(K * (K + 1) // 2 - sum(cand_A))
