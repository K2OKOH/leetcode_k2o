from typing import List
import sys

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n+1) for i in range(m+1)]
        dp[0][0] = True
        # s 为空的情况
        for j in range(1,n+1):
            if(p[j-1] == '*'):
                dp[0][j] = dp[0][j-2]
        # s 不为空
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(p[j-1] == '.'):
                    dp[i][j] = dp[i-1][j-1]
                elif(p[j-1] != '*'):
                    dp[i][j] = (dp[i-1][j-1] and (s[i-1] == p[j-1]))
                elif(p[j-2] != s[i-1] and p[j-2] != '.'):
                    dp[i][j] = dp[i][j-2]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i][j-2]
        
        return dp[m][n]


if __name__ == '__main__':
    s = "aa" 
    p = "a*"
    So = Solution()
    ans = So.isMatch(s, p)
    print(ans)