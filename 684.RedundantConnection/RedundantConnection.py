from typing import List

class UF:
    def __init__(self, n):
        self.idx = [a for a in range(n)]

    def find(self, p):
        while (p != self.idx[p]):
            p = self.idx[p]
        return p

    def connect(self, p: int, q: int):
        self.idx[self.find(p)] = self.find(q)

    def isConnect(self, p: int, q: int) -> bool:
        return (self.find(p) == self.find(q))


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n+1)
        for e in edges:
            u = e[0]
            v = e[1]
            # 查看 边是否已经连接 -> 已经连接去除该边
            if (uf.isConnect(u, v)):
                return e
            # 未连接 -> 连上
            uf.connect(u, v)
        # 没有重复连接的边
        return [-1, -1]

if __name__ == '__main__':
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]

    So = Solution()
    ans = So.findRedundantConnection(edges)
    print(ans)
