class Solution(object):
    # def maxProfit(self, prices):
    #     x= min(prices)
    #     sliced_list = prices[prices.index(x):]
    #     max_number = max(sliced_list)
    #     return max_number - x
   
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                max_profit = max(max_profit, current_profit)
        
        return max_profit
s = Solution()
print(s.maxProfit([2,4,1]))