from math import gcd

X, Y = map(int, input().split())


class LDE:
    # 初期化
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        self.m, self.x, self.y = 0, [0], [0]
        # 解が存在するか
        self.check = True
        g = gcd(self.a, self.b)
        if c % g != 0:
            self.check = False
        else:
            # ax+by=gの特殊解を求める
            self.extgcd(abs(self.a), abs(self.b), self.x, self.y)
            if a < 0:
                self.x[0] = -self.x[0]
            if b < 0:
                self.y[0] = -self.y[0]
            # ax+by=cの特殊解を求める
            self.x = self.x[0] * c // g
            self.y = self.y[0] * c // g
            # 一般解を求めるために
            self.a //= g
            self.b //= g

    # 拡張ユークリッドの互除法
    # 返り値:aとbの最大公約数
    def extgcd(self, a, b, x0, y0):
        if b == 0:
            x0[0], y0[0] = 1, 0
            return a
        d = self.extgcd(b, a % b, y0, x0)
        y0[0] -= (a // b) * x0[0]
        return d

    # パラメータmの更新(書き換え)
    def m_update(self, m):
        self.x += (m - self.m) * self.b
        self.y -= (m - self.m) * self.a
        self.m = m


r1 = LDE(X, -Y, 2)
r2 = LDE(X, -Y, -2)
if not (r1.check or r2.check):
    print(-1)
elif r1.check:
    print(r1.y, r1.x)
else:
    print(r2.y, r2.x)
