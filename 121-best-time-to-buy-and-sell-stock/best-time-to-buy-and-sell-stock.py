class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 #buy
        R = 1 #sell

        maxVal = 0
        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxVal = max(maxVal, profit)
            else:
                L = R
            R = R+1

        return maxVal