from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        minP = -sys.maxsize - 1
        for i in range(len(prices)):
            minP = max(minP, -prices[i])
            sell = max(sell, minP + prices[i])
        return sell

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    So = Solution()
    ans = So.maxProfit(prices)
    print(ans)
