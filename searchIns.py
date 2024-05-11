class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
            

    def lengthOfLastWord(self, s: str) -> int:
        s_len = len(s) - 1
        for i in range(s_len, -1, -1):
            if s[i].isalpha():
                s = s[:i+1]
                break
            
        s_len = len(s) - 1
        
        
        for i in range(s_len, -1, -1):
            if s[i] == ' ':
                return s_len - i
            if i == 0:
                return s_len + 1
        
sol = Solution()
inp = [1]
tar = 0
# print(sol.searchInsert(inp, tar))

s = "  fly  me  world    "
print(sol.lengthOfLastWord(s))
    
# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1