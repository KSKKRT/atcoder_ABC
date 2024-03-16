S = input()
mid = S[1 : len(S) - 1].replace("=", "")
flag = S[0] == "<" and len(mid) == 0 and S[-1] == ">"
print("Yes" if flag else "No")
