class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for idx in range(1, len(nums)): #O(n-1)
            nums[idx] = nums[idx-1] + nums[idx] #메모리 아끼기 
        
        return nums 
            