# -*- coding: utf-8 -*-


class Solution:

    cache = {}
    prices = None

    def dfs(self, idx):
        profit = self.cache.get(idx)
        if profit is not None:
            return profit

        profit = 0
        for i in range(idx, len(self.prices)):
            sell = self.prices[i]
            for j in range(i, len(self.prices)):
                if self.prices[j] > sell:
                    print(self.prices, self.prices[j], sell, profit)
                    profit = max(profit, self.prices[j] - sell + self.dfs(j + 1))
                    print(self.prices, self.prices[j], sell, profit)
        self.cache[idx] = profit
        return profit

    def dfsMaxProfit(self, prices) -> int:
        self.prices = prices
        return self.dfs(0)

    def maxProfit(self, prices) -> int:
        profit = 0
        for idx in range(len(prices) - 1):
            if prices[idx] < prices[idx + 1]:
                profit += (prices[idx + 1] - prices[idx])
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit([3, 2, 6, 5, 0, 3]))
