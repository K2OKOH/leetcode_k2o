from typing import List, Text

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Lx = len(matrix[0])
        Ly = len(matrix)
        ans = 0
        i = 0
        j = Lx - 1
        while(i<Ly and j>=0):
            print("%s,%s --> %s" %(i,j,matrix[i][j]))
            if(matrix[i][j] == target):
                return True
            elif(matrix[i][j] < target):
                i += 1
            elif(matrix[i][j] > target):
                j -= 1
        return False



if __name__ == '__main__':
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    So = Solution()
    ans = So.searchMatrix(matrix, target)
    print(ans)