from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        len_y = len(matrix)
        len_x = len(matrix[0])
        self.add_matrix = [[0]*(len_x+1) for i in range(len_y+1)]
        print(self.add_matrix)
        for idx_y in range(1,len_y+1):
            for idx_x in range(1,len_x+1):
                self.add_matrix[idx_y][idx_x] = self.add_matrix[idx_y-1][idx_x] \
                                         + self.add_matrix[idx_y][idx_x-1] \
                                         - self.add_matrix[idx_y-1][idx_x-1] \
                                         + matrix[idx_y-1][idx_x-1]
        print(self.add_matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.add_matrix[row2+1][col2+1] \
            + self.add_matrix[row1][col1] \
            - self.add_matrix[row1][col2+1] \
            - self.add_matrix[row2+1][col1]
        return ans


if __name__ == '__main__':
    matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
    row1 = 2
    col1 = 1
    row2 = 4
    col2 = 3
    So = NumMatrix(matrix)
    ans = So.sumRegion(row1,col1,row2,col2)
    print(ans)