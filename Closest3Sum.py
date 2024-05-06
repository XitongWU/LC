class Solution:
    def threeSumClosest(self, nums, target):
        gap0 = float('inf')
        result = 0  # Initialize result as an integer, not a list
        nums.sort()

        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                gap = abs(target - current_sum)

                if gap < gap0:
                    gap0 = gap
                    result = current_sum  # Update result with the current sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result


s = Solution()
num = [-1,2,1,-4]
tar = 1
print(s.threeSumClosest(num, tar))
