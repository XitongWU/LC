class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict = {}
        tdict = {}

        for cs in s:
            if sdict.get(cs) is None:
                sdict[cs] = 1
            else:
                sdict[cs] += 1
        
        for ct in t:
            if tdict.get(ct) is None:
                tdict[ct] = 1
            else:
                tdict[ct] += 1
        
        for key in sdict.keys():
            if tdict.get(key) is None:
                return False
            elif sdict[key] != tdict[key]:
                return False
            else:
                continue
        
        return True

    def missingNumber(self, nums: list[int]) -> int:
        set_nums = set()
        for i in range(len(nums) + 1):
            set_nums.add(i)
            
        for num in nums:
            set_nums.remove(num)
        
        return set_nums.pop()
        
    def findDuplicate(self, nums: list[int]) -> int:
        set_nums = set()
        for num in nums:
            if num in set_nums:
                return num
            set_nums.add(num)
        return 0
            
        
        
        
    

sol = Solution()
s = 'sat'
t = 'tar'
# print(sol.isAnagram(s, t))


# lst = [1,2,3,4,5]
# print(sol.missingNumber(lst))
        
lst = [1,2,3,4,4,5,6,7]
print(sol.findDuplicate(lst))
        
            