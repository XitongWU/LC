class Solution:
    # def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
    #     def isDup(numLst:list[int]) -> bool:
    #         num_set = set()
    #         for num in numLst:
    #             if num in num_set:
    #                 return True
    #             num_set.add(num)
    #         return False
        
    #     is_dup = False
    #     for i in range(0, max(len(nums) - k + 1, 1)):
    #         is_dup = is_dup or isDup(nums[i: min(i + k + 1, len(nums))])
    #     return is_dup
    
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        index_dict = {}
        
        for i in range(0, len(nums)):
            if index_dict.get(nums[i]) is None:
                index_dict[nums[i]] = [i]
            else:
                for index in reversed(index_dict[nums[i]]):
                    if i - index <= k:
                        return True
                index_dict[nums[i]].append(i)
        return False
               
                
        
        
            

sol = Solution()
inp = [2,2]
k = 3
print(sol.containsNearbyDuplicate(inp,k))
    
    