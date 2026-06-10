class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfix to compute all the profix we made
        # 1 pointers for buy 
        # with buy starting at day 1

        # while buy < sell:
        # 1. Compute the profix = the price of next day minus the price of current day
        #   a. If there is profix, add up that profix to maxProfix.
        # 2. We move buy pointer forward by increasing by 1.
        # Return maxProfix

        # Time complexity: O(n) with n represents for the number of prices
        # Space complexity: O(1)

        # sell = buy + 1 
        buy, maxProfix = 0, 0
        while buy < len(prices) -1:
            if prices[buy+1] - prices[buy] > 0:
                maxProfix += (prices[buy+1] - prices[buy])
            buy += 1
        return maxProfix
                 