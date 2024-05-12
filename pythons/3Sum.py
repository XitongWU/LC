class Solution:
    def threeSum(self, nums:list[int]) -> list[list[int]]:
        res_lst:list[list[int]] = []
        
        nums.sort()
        
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res_lst.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        
        return res_lst


nums = [0,0,0]
s = Solution()
print(s.threeSum(nums))
