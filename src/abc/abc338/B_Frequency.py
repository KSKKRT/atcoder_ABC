freq_list = [0 for _ in range(26)]
S = input()
base = ord('a')
for i in range(len(S)):
    freq_list[ord(S[i]) - base] += 1
ans_idx = freq_list.index(max(freq_list))
print(chr(base + ans_idx))
