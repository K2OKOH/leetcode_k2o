from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        H = len(grid)
        W = len(grid[0])
        dp = [[0] * W] * H
        for idx_y in range(H):
            for idx_x in range(W):
                if(idx_x == 0 and idx_y == 0):
                    dp[idx_y][idx_x] = grid[idx_y][idx_x]
                elif(idx_x == 0):
                    dp[idx_y][idx_x] = dp[idx_y-1][idx_x] + grid[idx_y][idx_x]
                elif(idx_y == 0):
                    dp[idx_y][idx_x] = dp[idx_y][idx_x-1] + grid[idx_y][idx_x]
                else:
                    dp[idx_y][idx_x] = min(dp[idx_y-1][idx_x],dp[idx_y][idx_x-1]) + grid[idx_y][idx_x]
        return dp[H-1][W-1]
         

if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    So = Solution()
    ans = So.minPathSum(grid)
    print(ans)
