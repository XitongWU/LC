class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        num_dict = {nums[0]:1}
        for i in range(1, len(nums)):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = 1
            else:
                num_dict[nums[i]] += 1
        
        for key in num_dict:
            if num_dict[key] == 1:
                return key
                
                
                
                
                
                