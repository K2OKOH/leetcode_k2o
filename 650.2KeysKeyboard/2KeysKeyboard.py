from typing import List

class Solution:
    def minSteps(self, n: int) -> int:
        h = int(n ** 0.5)
        dp = [0] * (n+1)
        for i in range(2,n+1):
            dp[i] = i
            for j in range(2,h+1):
                if(i%j == 0):
                    dp[i] = dp[j] + dp[int(i/j)]
                    break
        return dp[n]

if __name__ == '__main__':
    n = 4
    So = Solution()
    ans = So.minSteps(n)
    print(ans)
