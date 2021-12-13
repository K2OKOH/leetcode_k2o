from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        list_temp = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                list_temp[i][j] = matrix[n-i-1][j]
        # print(list_temp)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = list_temp[j][i]


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    So = Solution()
    So.rotate(matrix)
    print(matrix)