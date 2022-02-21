from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # 如果没有结点 -> 算事可以二分
        if (n == 0):
            return True
        color = [0] * n
        q = []
        for idx in range(n):
            # 如果该点没有被上色 -> 放入队列中（起始点处理）
            if (color[idx] == 0):
                q.append(idx)
                color[idx] == 1
            # 取出队列中的第一个
            while(len(q) != 0):
                node = q[0]
                q.pop(0)
                # 遍历该 node 的连接
                for j in graph[node]:
                    if (color[j] == 0):
                        q.append(j)
                        # 根据当前结点，给相邻的结点上不同的色彩
                        if (color[node] == 2):
                            color[j] = 1
                        else:
                            color[j] = 2
                    # 如果当前结点 和 相邻结点 颜色相同 -> 不可二分
                    elif (color[node] == color[j]):
                        return False
        # 当队列已清空 -> 可以二分
        return True

if __name__ == '__main__':
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]

    So = Solution()
    ans = So.isBipartite(graph)
    print(ans)
