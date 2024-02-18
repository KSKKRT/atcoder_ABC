N = int(input())
result = ["1" for _ in range(2 * N + 1)]
for i in range(1, len(result), 2):
    result[i] = "0"
print("".join(result))
