class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfix to compute all the profix we made
        # 2 pointers for buy and sell 
        # with buy starting at day 1
        # with sell starting at day 2

        # while buy < sell:
        # 1. If the price of buy is lower than the price of sell, 
        #   a. Compute the profix = the sell price minus the buy price.
        #   b. Then, We can add up that profix to maxProfix.
        # 2. We move buy and sell pointers forward by increasing by 1.
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
                 