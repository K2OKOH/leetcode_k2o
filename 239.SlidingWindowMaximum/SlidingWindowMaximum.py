from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        ans = []
        for n in nums:
            queue.append(n)
            if (len(queue) >= k):
                ans.append(max(queue))
                queue.pop(0)
        return ans

if __name__ == '__main__':
    # 初始化数组
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    
    So = Solution()
    ans = So.maxSlidingWindow(nums, k)
    print(ans)