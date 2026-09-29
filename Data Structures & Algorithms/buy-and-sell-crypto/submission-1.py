class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        buy_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > buy_price:
                if prices[i] - buy_price > max_profit:
                    max_profit = prices[i] - buy_price
            else:
                buy_price = prices[i]
        
        return max_profit