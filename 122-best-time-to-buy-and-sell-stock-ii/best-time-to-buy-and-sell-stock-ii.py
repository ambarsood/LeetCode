class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        if not prices:
            return pofit

        buy = prices[0]

        for price in prices[1:]:
            if price < buy:
                buy = price
            else:
                profit += price - buy
                buy = price

        return profit