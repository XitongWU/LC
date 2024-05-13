class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        
        global_max = nums[0]
        
        i = 0
        while i <= global_max:
            global_max = max(global_max, i + nums[i])
            i += 1
            if global_max >= len(nums) - 1:
                return True
        
        return False
    
sol = Solution()
nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
print(sol.canJump(nums))
            