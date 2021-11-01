from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        num_1 = len(word1)
        num_2 = len(word2)
        dp = [[0] * (num_2+1) for i in range(num_1+1)]
        for idx_y in range(num_1+1):
            for idx_x in range(num_2+1):
                if(idx_x == 0):
                    dp[idx_y][idx_x] = idx_y
                elif(idx_y == 0):
                    dp[idx_y][idx_x] = idx_x
                else:
                    dp[idx_y][idx_x] = min(min(dp[idx_y][idx_x-1]+1, dp[idx_y-1][idx_x]+1), dp[idx_y-1][idx_x-1] if(word1[idx_y-1] == word2[idx_x-1]) else dp[idx_y-1][idx_x-1]+1)

        return dp[num_1][num_2]

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    So = Solution()
    ans = So.minDistance(word1, word2)
    print(ans)
