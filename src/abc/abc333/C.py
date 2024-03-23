N = int(input())
rep = [int("1" * i) for i in range(1, 13)]
res_list = []
for i in range(len(rep)):
    for j in range(len(rep)):
        for k in range(len(rep)):
            tmp = rep[i] + rep[j] + rep[k]
            if tmp not in res_list:
                res_list.append(rep[i] + rep[j] + rep[k])
res_list = sorted(res_list)
print(res_list[N - 1])
