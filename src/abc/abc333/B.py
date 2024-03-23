S = input()
T = input()


def near(a: str):
    s = ["A", "B", "C", "D", "E"]
    dis = abs(s.index(a[0]) - s.index(a[1]))
    return dis == 1 or dis == 4


print("Yes" if near(S) == near(T) else "No")
