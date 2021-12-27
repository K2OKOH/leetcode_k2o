from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        ans = []
        for idx in range(len(nums)):
            # 把超出窗的序号去除
            if (len(queue) != 0 and queue[0] == idx-k):
                queue.pop(0)
            # 把小于当前值的数去除
            while (len(queue) != 0 and nums[queue[-1]] < nums[idx]):
                queue.pop()
            # 把当前序号加入队列
            queue.append(idx)
            # 把队列中的第一个数放入ans中
            if (idx >= k - 1):
                ans.append(nums[queue[0]])
        return ans

if __name__ == '__main__':
    # 初始化数组
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    
    So = Solution()
    ans = So.maxSlidingWindow(nums, k)
    print(ans)