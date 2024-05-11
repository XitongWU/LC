class Solution:
    def maxProfit(self, prices):
        # buy = prices[0]
        # profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i] < buy:
        #         buy = prices[i]
        #     elif prices[i] - buy > profit:
        #         profit = prices[i] - buy
        # return profit
        
        minBuy = prices[0]
        maxProf = 0
        for i in range(1, len(prices)):
            if prices[i-1] < minBuy:
                minBuy = prices[i-1]
            if prices[i] - minBuy > maxProf:
                maxProf = prices[i] - minBuy
                
        return maxProf
            
        
        pass
    
    
    
    
    
    
    