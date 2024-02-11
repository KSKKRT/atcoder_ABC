N = int(input())
v: list[list] = [[] for _ in range(2 * N)]
for i in range(N):
    a, b = map(lambda x: int(x) - 1, input().split())
    if a > b:
        a, b = b, a
    v[a] = [0, i]
    v[b] = [1, i]

stack = []
flag = False
for i in range(2 * N):
    t, id = v[i]
    if not t:
        stack.append(id)
    else:
        if stack[-1] != id:
            flag = True
            break
        stack.pop()
print('Yes' if flag else 'No')
