from typing import List
import sys

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        day = len(prices)
        dp_buy = [-sys.maxsize] * (k+1)
        dp_sell = [0] * (k+1)
        if(day < 2):
            return 0
        if (k >= day):
            sum = 0
            for i in range(1,k):
                if(prices[i-1]<prices[i]):
                    sum += prices[i] - prices[i-1]
            return sum
        for i in range(day):
            for j in range(1,k+1):
                dp_buy[j] = max(dp_buy[j], dp_sell[j-1] - prices[i])
                dp_sell[j] = max(dp_sell[j], dp_buy[j] + prices[i])
        return dp_sell[k]

if __name__ == '__main__':
    prices = [3,2,6,5,0,3]
    k = 2
    So = Solution()
    ans = So.maxProfit(k, prices)
    print(ans)
