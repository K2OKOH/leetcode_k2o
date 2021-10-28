from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for i in range(m+1)] 
        for s in strs:
            n0 = s.count('0')
            n1 = s.count('1')
            for i in range(m,n0-1,-1):
                for j in range(n,n1-1,-1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-n0][j-n1])
        return dp[m][n]

if __name__ == '__main__':
    strs = ["10","0001","111001","1","0"]
    m = 5
    n = 3
    So = Solution()
    ans = So.findMaxForm(strs, m, n)
    print(ans)
