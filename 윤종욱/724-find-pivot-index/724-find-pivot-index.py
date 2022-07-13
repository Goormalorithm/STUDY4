class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        if not nums:
            return nums
        
        leftSum = 0
        totalSum = sum(nums)
        
        for i in range(len(nums)):
            diff = totalSum - nums[i] - leftSum
            
            if diff == leftSum:
                return i
            
            leftSum += nums[i]
            
        return -1