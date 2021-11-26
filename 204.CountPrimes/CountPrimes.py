from typing import List

class Solution:
    def countPrimes(self, n: int) -> int:
        if(n<2):
            return 0
        prime = [True] * n
        count = n-2
        for idx in range(2,n):
            if(prime[idx]):
                for jdx in range(2*idx,n,idx):
                    if(prime[jdx]):
                        prime[jdx] = False
                        count -= 1
        return count

if __name__ == '__main__':
    n = 10
    So = Solution()
    ans = So.countPrimes(n)
    print(ans)
