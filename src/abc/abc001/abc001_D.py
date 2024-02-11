time = [0 for _ in range(2401)]
N = int(input())
for _ in range(N):
    s, e = map(int, input().split("-"))
    time[s:e+1] = [1 for _ in range(e-s)]
i = 0
while i < len(time):
    s = ""
    e = ""
    if time[i]: s = str(i).zfill(4)
    while time[i]:
        i += 1
    else:
        t = str(i-1).zfill(4)
        print(f"{s}-{e}")
    i += 1