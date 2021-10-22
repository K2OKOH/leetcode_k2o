from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_1 = len(text1)
        len_2 = len(text2)
        dp = [[0] * (len_2+1) for n in range(len_1+1)]
        for i in range(1,len_1+1):
            for j in range(1,len_2+1):
                if(text1[i-1] == text2[j-1]):
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len_1][len_2]

if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    So = Solution()
    ans = So.longestCommonSubsequence(text1, text2)
    print(ans)
