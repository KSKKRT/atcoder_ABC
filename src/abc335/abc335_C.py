N, Q = map(int, input().split())
pos = [[i, 0] for i in range(N + 1, 0, -1)]
for _ in range(Q):
    q, c = input().split()
    if q == "1":
        tmp = pos[-1][::]
        if c == "R":
            tmp[0] += 1
        elif c == "L":
            tmp[0] -= 1
        elif c == "U":
            tmp[1] += 1
        elif c == "D":
            tmp[1] -= 1
        pos.append(tmp)
    elif q == "2":
        print(*pos[-int(c)])
