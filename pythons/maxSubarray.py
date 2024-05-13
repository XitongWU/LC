class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        local_max = nums[0]
        global_max = nums[0]
        
        for num in nums[1:]:
            local_max = max(num, num + local_max)
            global_max = max(global_max, local_max)
            
        return global_max
        