class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]

        left = 0
        right = 0
        res = []
        while left < len(nums) and right < len(nums):
            if right == len(nums) - 1 or nums[right + 1] - nums[right] > 1:
                if right - left == 0:
                    res.append(str(nums[left]))
                else:
                    res.append(str(nums[left]) + "->" + str(nums[right]))
                right += 1
                left = right
            else:
                right += 1
        
        return res
    
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        bin_str = bin(n)[2:]
        pow = len(bin_str) - 1
        if n == 2 ** pow:
            return True
        else:
            return False
    
    def isPerfectSquare(self, num: int) -> bool:
        
        pass
    
sol = Solution()
# lst = [0,1,2,4,5,7]
# print(sol.summaryRanges(lst))

n = 16
print(sol.isPowerOfTwo(n))