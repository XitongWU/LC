class Solution:
    def searchRange(self, nums, target):
        def binary_search_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def binary_search_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left_idx = binary_search_left(nums, target)
        right_idx = binary_search_right(nums, target)
        
        if left_idx <= right_idx:
            return [left_idx, right_idx]
        else:
            return [-1, -1]
    
    
sol = Solution()
nums = [7,8,9,9,9,10]
target = 9
print(sol.searchRange(nums, target))
# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]