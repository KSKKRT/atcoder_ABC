class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = [-1 for _ in range(n)] #親頂点の番号を保存
        self.size = [1 for _ in range(n)] #各頂点の所属する根付き木のサイズ

    # 頂点xの値を求める
    def root(self, x: int) -> int:
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x]) #経路圧縮
            return self.par[x]

    # 2頂点x, yの所属する木の根が一致するか 
    def issame(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)
    
    # xを含む木とyを含む木を結合する(返り値はすでに同一グループか否か)
    def unite(self, x: int, y: int) -> bool:
        rootx: int = self.root(x)
        rooty: int = self.root(y)
        if rootx == rooty:
            return False
        if self.size[rootx] < self.size[rooty]:
            rootx, rooty = rooty, rootx # Union by Sizeのためにxの方が頂点数が多くなる様にする
        self.par[rooty] = rootx
        self.size[rootx] += self.size[rooty]
        return True
    
    # xを含む木のサイズを求める
    def get_size(self, x: int) -> int:
        return self.size[self.root(x)]


if __name__ == '__main__':
    # ユースケース -> クラスカル法
    # edge: (weight, node1, node2)
    edges = [
        (5, 0, 3),
        (3, 0, 7),
        (6, 0, 5),
        (8, 1, 3),
        (4, 1, 4),
        (3, 1, 6),
        (9, 2, 4),
        (10, 2, 5),
        (5, 2, 7),
        (6, 3, 7),
        (2, 4, 6),
        (7, 6, 7)
    ]
    N = 8 #頂点数
    M = len(edges) #辺数
    uf = UnionFind(N)
    edges = sorted(edges, key=lambda x: x[0])
    minimum_cost = 0
    for i in range(M):
        w, u, v = edges[i]
        if uf.issame(u, v): continue
        uf.unite(u, v)
        minimum_cost += w
    print(minimum_cost) # 最小全域木のコストが求まる




        
