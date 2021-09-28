from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        dp[1] = nums[0]
        for i in range(2,n+1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
        return dp[n]

if __name__ == '__main__':
    nums = [1,2,3,1]
    So = Solution()
    ans = So.rob(nums)
    print(ans)
