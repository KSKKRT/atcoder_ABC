N = int(input())
ctz = 0
while True:
    if N % 2 == 0:
        N //= 2
        ctz += 1
    else:
        break
print(ctz)