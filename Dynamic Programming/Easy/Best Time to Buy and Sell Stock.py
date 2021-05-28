class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        num = float('inf')
        for i in range(0, len(prices)):
            
            if prices[i] - num > maxi:
                maxi = prices[i] - num
            if prices[i] < num:
                num = prices[i]
            
        return maxi
