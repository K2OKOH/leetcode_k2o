from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        H = len(mat)
        W = len(mat[0])
        dp = [[99999] * W for i in range(H)]
        for idx_y in range(H):
            for idx_x in range(W):
                if(mat[idx_y][idx_x] == 0):
                    dp[idx_y][idx_x] = 0
                else:
                    if (idx_x > 0):
                        dp[idx_y][idx_x] = min(dp[idx_y][idx_x], dp[idx_y][idx_x-1] + 1)
                    if (idx_y > 0):
                        dp[idx_y][idx_x] = min(dp[idx_y][idx_x], dp[idx_y-1][idx_x] + 1)
        
        for idx_y in range(H)[::-1]:
            for idx_x in range(W)[::-1]:
                if(mat[idx_y][idx_x] != 0):
                    if (idx_x < W-1):
                        dp[idx_y][idx_x] = min(dp[idx_y][idx_x], dp[idx_y][idx_x+1] + 1)
                    if (idx_y < H-1):
                        dp[idx_y][idx_x] = min(dp[idx_y][idx_x], dp[idx_y+1][idx_x] + 1)
        return dp

if __name__ == '__main__':
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    So = Solution()
    ans = So.updateMatrix(mat)
    print(ans)
