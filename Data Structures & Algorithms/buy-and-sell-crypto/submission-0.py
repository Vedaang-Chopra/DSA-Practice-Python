class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit =0 
        buy_i=0
        sell_i=0
        while sell_i<len(prices):
            current_profit = prices[sell_i] - prices[buy_i]
            if current_profit > max_profit and current_profit>0:
                max_profit = current_profit
            if prices[sell_i] < prices[buy_i]:
                buy_i=sell_i
            
            sell_i+=1
        
        return max_profit