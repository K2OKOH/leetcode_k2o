from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        return ans


if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    So = Solution()
    ans = So.maximalSquare(matrix)
    print(ans)
