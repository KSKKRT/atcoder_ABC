H, W, N = map(int, input().split())
A = [['.' for _ in range(W)] for _ in range(H)]
right, left, down = False, False, False
i, j = 0, 0
for _ in range(N):
    if A[i][j] == '#':
        A[i][j] = '.'
        rev = 1
    else:
        A[i][j] = '#'
        rev = -1
    if right:
        i -= rev
        right = False
        down = rev == -1
    elif left:
        i += rev
        left = False
        down = rev == 1
    elif down:
        j += rev
        down = False
        right = rev == 1
        left = rev == -1
    else:
        j -= rev
        right = rev == -1
        left = rev == 1
    if i == -1:
        i = H - 1
    if i == H:
        i = 0
    if j == -1:
        j = W - 1
    if j == W:
        j = 0

for r in A:
    print(*r, sep='')
