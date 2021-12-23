from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        priority_heap =[]
        idx = 0
        b_len = len(buildings)
        cur_x = 0
        cur_y = 0
        while(idx < b_len or len(priority_heap)!=0):
            # 当前左 < 最高右
            # if (priority_heap != []):
            #     print(heapq.nlargest(1, priority_heap)[0][1])
            if ((len(priority_heap) == 0) or idx < b_len and buildings[idx][0] <= heapq.nlargest(1, priority_heap)[0][1]):
                # 取当前左值
                cur_x = buildings[idx][0]
                while (idx < b_len and cur_x == buildings[idx][0]):
                    # 把 (右, 高) 放入堆中
                    heapq.heappush(priority_heap,[buildings[idx][2], buildings[idx][1]])
                    idx += 1
            # 当前左 > 最高右
            else:
                # 取最高 右值
                cur_x = heapq.nlargest(1, priority_heap)[0][1]
                # 把 <= 最高 右 的去除
                while ((len(priority_heap) != 0) and cur_x >= heapq.nlargest(1, priority_heap)[0][1]):
                    priority_heap.remove(heapq.nlargest(1, priority_heap)[0])
            cur_y = heapq.nlargest(1,priority_heap)[0][0] if (priority_heap != []) else 0
            # 如果 ans 变化了, 添加更新
            if (ans == [] or cur_y != ans[-1][1]):
                ans.append([cur_x, cur_y])
        return ans

if __name__ == '__main__':
    # 初始化数组
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    
    So = Solution()
    ans = So.getSkyline(buildings)
    print(ans)