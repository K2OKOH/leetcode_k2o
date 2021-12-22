# Definition for singly-linked list.
from heapq import heappop, heappush
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 获取楼房个数
        b_length = len(buildings)
        # 把右顶点进行排序
        right_point = []
        for build in buildings:
            right_point.append(build[1::])
        print(right_point)
        priority_heap = []
        heappush(priority_heap, right_point)

        # 加入第一个左定点，并pop排序完成的右顶点
        


if __name__ == '__main__':
    # 初始化数组
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    
    So = Solution()
    ans = So.getSkyline(buildings)
    print(ans)