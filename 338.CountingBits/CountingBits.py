from collections import defaultdict
from typing import List
import itertools

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1,n+1):

            ans[i] = ans[i-1] + 1 if (i & 1) else ans[i>>1]

        return ans


if __name__ == '__main__':
    n = 5
    So = Solution()
    ans = So.countBits(n)
    print(ans)