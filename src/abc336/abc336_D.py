N = int(input())
A = list(map(int, input().split()))
res = 0

if N <= 2:
    res = 1
while True:
    if  N % 2 == 1:
        for i in range((N-1)//2):
            if A[i] < i+1:
                break


