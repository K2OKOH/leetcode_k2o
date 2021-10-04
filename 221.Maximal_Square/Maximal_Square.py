from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        H = len(matrix)
        W = len(matrix[0])
        if(H==0 or W==0):
            return 0
        dp = [[0]*W for i in range(H)]
        for idx_y in range(H):
            for idx_x in range(W):
                if(matrix[idx_y][idx_x] != '0'):
                    dp[idx_y][idx_x] = min(dp[idx_y-1][idx_x-1], min(dp[idx_y-1][idx_x],dp[idx_y][idx_x-1])) + 1
                ans = max(ans, dp[idx_y][idx_x])
        return ans*ans


if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    So = Solution()
    ans = So.maximalSquare(matrix)
    print(ans)
