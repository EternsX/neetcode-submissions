class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        res = 0

        for p in prices:
            res = max(res, p - minBuy)
            minBuy = min(minBuy, p)
        return res

