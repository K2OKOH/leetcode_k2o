from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums)%2):
            return False
        half_sum = int(sum(nums)/2)
        n = len(nums)
        dp = [[False] * (half_sum+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1,n+1):
            for j in range(1,half_sum+1):
                if(j>=nums[i-1]):
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][half_sum]

if __name__ == '__main__':
    nums = [1,5,10,6]
    So = Solution()
    ans = So.canPartition(nums)
    print(ans)
