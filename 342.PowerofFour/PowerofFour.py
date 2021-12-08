from typing import List

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        judge = 0
        for i in range(0,32,2):
            # print(i)
            judge |= 1<<i
        # print(bin(judge))
        if((judge & n == n) and (n & n-1 == 0) and (n > 0)):
            return True
        else:
            return False

if __name__ == '__main__':
    n = 5
    So = Solution()
    ans = So.isPowerOfFour(n)
    print(ans)
