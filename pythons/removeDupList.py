class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        left = 0
        right = 1
        cur_length = len(nums)
        
        while right < cur_length:
            while right < cur_length and nums[left] == nums[right]:
                nums.pop(right)
                cur_length -= 1
            left += 1
            right += 1
            
        return cur_length
            
        
        pass
    

sol = Solution()
nums = [1,1,1,1,2,3,4,5,5,5,5,5,5,5]
print(sol.removeDuplicates(nums))