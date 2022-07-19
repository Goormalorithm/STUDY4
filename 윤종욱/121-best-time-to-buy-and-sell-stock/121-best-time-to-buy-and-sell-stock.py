class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_p = prices[0]
        max_diff = 0
        for price in prices[1:]:
            if min_p >= price:
                min_p = price
                continue
            else:
                max_diff = max(max_diff, price - min_p)
                
        return max_diff
                
            