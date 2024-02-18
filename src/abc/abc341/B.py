N = int(input())
A = list(map(int, input().split()))
carry = 0
for i in range(N - 1):
    s, t = map(int, input().split())
    A[i] += carry
    carry = (A[i] // s) * t
print(A[-1] + carry)
