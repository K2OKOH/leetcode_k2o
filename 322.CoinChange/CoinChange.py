from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [amount+2] * (amount+1)
        dp[0] = 0
        for i in range(1,n+1):
            for j in range(coins[i-1],amount+1):
                dp[j] = min(dp[j], dp[j-coins[i-1]] + 1)
        if (dp[amount] == amount+2):
            return -1
        return dp[amount]

if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    So = Solution()
    ans = So.coinChange(coins, amount)
    print(ans)
