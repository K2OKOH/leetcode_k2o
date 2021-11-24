from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_l = len(prices)
        if(prices_l==0):
            return 0
        dp_buy = [0]*prices_l
        dp_sell = [0]*prices_l
        dp_s1 = [0]*prices_l
        dp_s2 = [0]*prices_l
        dp_buy[0] = dp_s1[0] = -prices[0]
        dp_sell[0] = dp_s2[0] = 0
        for idx in range(1,prices_l):
            dp_buy[idx] = dp_s2[idx-1] - prices[idx]
            dp_s1[idx] = max(dp_s1[idx-1], dp_buy[idx-1])
            dp_sell[idx] = max(dp_s1[idx-1], dp_buy[idx-1]) + prices[idx]
            dp_s2[idx] = max(dp_s2[idx-1], dp_sell[idx-1])
        return max(dp_sell[prices_l-1], dp_s2[prices_l-1])
            

if __name__ == '__main__':
    prices = [1]
    So = Solution()
    ans = So.maxProfit(prices)
    print(ans)
