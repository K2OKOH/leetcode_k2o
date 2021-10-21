from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_l = 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if(nums[i] > nums[j]):
                    dp[i] = max(dp[i],dp[j]+1)
            max_l = max(max_l,dp[i])
        return max_l

if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    So = Solution()
    ans = So.lengthOfLIS(nums)
    print(ans)
