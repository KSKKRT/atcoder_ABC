A = []
while True:
    n = int(input())
    A.append(n)
    if n == 0:
        break
for n in A[::-1]:
    print(n)
