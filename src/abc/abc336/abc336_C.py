import re


def pen2dec(pen: str) -> str:
    res = re.sub("4", "8", pen)
    res = re.sub("3", "6", res)
    res = re.sub("2", "4", res)
    res = re.sub("1", "2", res)
    return res

N = int(input())
dec = N-1
pen = ""
while dec > 0:
    pen += str(dec % 5)
    dec = dec // 5
res = pen2dec(pen[::-1])
print(0 if N==1 else res)
