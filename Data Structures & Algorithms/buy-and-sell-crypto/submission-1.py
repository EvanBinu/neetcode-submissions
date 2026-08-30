class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        l,r = 0,1
        val = 0
        while r < n:
            val  = max(val,prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
                r+=1
            else:
                r+=1
            
        return val