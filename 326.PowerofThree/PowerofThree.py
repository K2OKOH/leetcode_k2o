from typing import List

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while(n>=3):
            if(n%3 != 0):
                return False
            else:
                n = n//3
        if(n==1):
            return True
        else:
            return False

if __name__ == '__main__':
    n = 6
    So = Solution()
    ans = So.isPowerOfThree(n)
    print(ans)
