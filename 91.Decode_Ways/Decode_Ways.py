from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s))
        for i in range(len(s)):
            if(i == 0):
                if(int(s[i]) == 0):
                    return 0
                dp[i] = 1
            elif(i == 1):
                b1 = int(s[i-1])
                b0 = int(s[i])
                if(b1 > 0 and b1*10+b0 <= 26 and b0 != 0):
                    dp[i] = 2
                elif((b1 == 0 or b1*10+b0 > 26) and b0 == 0):
                    return 0
                else:
                    dp[i] = 1
            else:
                b1 = int(s[i-1])
                b0 = int(s[i])
                if(b1 > 0 and b1*10+b0 <= 26 and b0 != 0):
                    dp[i] = dp[i-2] + dp[i-1]
                elif(b1 > 0 and b1*10+b0 <= 26 and b0 == 0):
                    dp[i] = dp[i-2]
                elif((b1 == 0 or b1*10+b0 > 26) and b0 != 0):
                    dp[i] = dp[i-1]
                else:
                    return 0
        return dp[len(s)-1]


if __name__ == '__main__':
    s = "1212"
    So = Solution()
    ans = So.numDecodings(s)
    print(ans)
