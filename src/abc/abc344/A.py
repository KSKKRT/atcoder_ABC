S = input()
idx = []
for i in range(len(S)):
    if S[i] == "|":
        idx.append(i)
result = S[: idx[0]] + S[idx[1] :]
result = result.replace("|", "")
print(result)
