from typing import List

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

if __name__ == '__main__':
    x = 1
    y = 4
    So = Solution()
    ans = So.hammingDistance(x, y)
    print(ans)
