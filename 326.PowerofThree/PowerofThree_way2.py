from typing import List
import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return math.fmod(math.log10(n)/math.log10(3),1) == 0

if __name__ == '__main__':
    n = 6
    So = Solution()
    ans = So.isPowerOfThree(n)
    print(ans)
