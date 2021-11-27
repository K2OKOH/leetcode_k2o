from typing import List

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if(n == 0):
            return 0
        else:
            return n//5 + self.trailingZeroes(n//5)

if __name__ == '__main__':
    n = 10
    So = Solution()
    ans = So.trailingZeroes(n)
    print(ans)
