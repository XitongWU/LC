class Solution:
    def threeSum(self, nums):
        # if len(nums)<3 or len(nums)>3000:
        #     return []
        # for i in range(len(nums)):
        #     if nums[i] < -10**5 or nums[i] > 10**5:
        #         return []

        tups_lst = []
        nums = sorted(nums)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        onetup = [nums[i],nums[j],nums[k]]
                        is_in = 0
                        for m in range(len(tups_lst)):
                            if set(tups_lst[m]) == set(onetup):
                                is_in = 1
                                break
                        if not is_in:
                            tups_lst.append(onetup)

        return tups_lst


nums = [0,0,0]
s = Solution()
print(s.threeSum(nums))
