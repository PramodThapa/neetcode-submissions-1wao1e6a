class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for price in prices:
            profit = max(profit, price - buy_price)
            buy_price = min(buy_price, price)

        return profit