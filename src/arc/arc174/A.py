N, C = map(int, input().split())
A = list(map(int, input().split()))


def max_subarray_sum(A):
    max_sum = -(10**10)
    cur_sum = 0

    for a in A:
        cur_sum = max(cur_sum + a, a)
        max_sum = max(max_sum, cur_sum)

    return max_sum


if C > 0:
    res = sum(A) + (C - 1) * max_subarray_sum(A)
else:
    tmp = list(map(lambda x: -x, A))
    res = sum(A) + (C - 1) * max_subarray_sum(tmp) * -1

print(max(sum(A), res))
