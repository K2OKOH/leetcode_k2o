from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        res = []
        # 统计接序情况 和 入度
        for pr in prerequisites:
            graph[pr[1]].append(pr[0])
            indegree[pr[0]] += 1
        q = []
        # 找到起始点：入度为0
        for i in range(len(indegree)):
            # 如果结点入度为0
            if (indegree[i] == 0):
                q.append(i)
        # 从入度为0的点开始,已经无时退出
        while (len(q) != 0):
            # 取最先进入的 入度为0 的结点
            u = q[0]
            res.append(u)
            q.pop(0)
            # 需要在入度为0的node 后的node 入度 -1
            for v in graph[u]:
                indegree[v] -= 1
                # 如果出现新的入度为0的点，加入队列
                if (indegree[v] == 0):
                    q.append(v)
        
        # 如果 入度 不都为0. 说明有环，返回[]
        for i in range(len(indegree)):
            if (indegree[i] != 0):
                return []
        return res

if __name__ == '__main__':
    # numCourses = 4
    # prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    numCourses = 2
    prerequisites = []

    So = Solution()
    ans = So.findOrder(numCourses, prerequisites)
    print(ans)
