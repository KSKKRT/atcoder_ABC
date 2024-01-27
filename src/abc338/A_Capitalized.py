S = input()
flag = S[0].capitalize() == S[0] and S[1:] == S[1:].lower()
print('Yes' if flag else 'No')
