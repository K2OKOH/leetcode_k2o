from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if(n<3):
            return 0
        dp = [0]*n
        for i in range(2,n):
            if(nums[i-2]-nums[i-1] == nums[i-1]-nums[i]):
                dp[i] = dp[i-1] + 1
        return sum(dp)

if __name__ == '__main__':
    nums = [1,2,3,4]
    So = Solution()
    ans = So.numberOfArithmeticSlices(nums)
    print(ans)
