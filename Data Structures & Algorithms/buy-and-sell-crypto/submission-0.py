class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        i = 0
        j = 1
        while j < n:
            # checks for max profit
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
            
            # logic for moving pointers

            #if no profit could be made from (i,j)
            if profit <= 0:
                i += 1
                # ensures i and j don't overlap
                if i == j:
                    j += 1
            
            # if there was profit, moves j along
            elif profit > 0:
                j += 1
        

        return max_profit

