class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = [0] * len(prices)
        prev = 100
        for i in range(len(prices)):
            l[i] = min(prev, prices[i])
            prev = l[i]
        
        r = [0] * len(prices)
        prev = 0
        for i in range(len(prices)-1, 0, -1):
            r[i] = max(prev, prices[i])
            prev = r[i]
        
        res = 0
        for i in range(len(prices)):
            res = max(res, r[i] - l[i])
        
        return res