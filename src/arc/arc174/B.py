T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    P = list(map(int, input().split()))
    stars = sum([(i + 1) * v for i, v in enumerate(A)])
    reviews = sum(A)
    p = 10**20
    if stars >= 3 * reviews:
        print(0)
        continue
    d = 3 * reviews - stars
    p = min(p, d * P[3])
    if d % 2 == 0:
        p = min(p, P[3] + ((d - 1) // 2 + 1) * P[4])
        p = min(p, d // 2 * P[4])
    else:
        p = min(p, P[3] + ((d - 1) // 2) * P[4])
        p = min(p, (d // 2 + 1) * P[4])
    print(p)
