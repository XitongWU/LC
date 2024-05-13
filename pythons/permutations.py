class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        import copy
        res_lst:list[list[int]] = []
        is_used:list[int] = [0] * len(nums)
        # print(is_used)
        cur_res:list[int] = []
        
        def DFS(cur_res:list[int]) ->None:
            nonlocal is_used, res_lst
            if len(cur_res) == len(is_used):
                res_lst.append(copy.deepcopy(cur_res))
                return
            
            for i in range(len(is_used)):
                if is_used[i] == 0:
                    is_used[i] = 1
                    cur_res.append(nums[i])
                    DFS(cur_res)
                    cur_res.pop()
                    is_used[i] = 0
        
        DFS(cur_res)
        return res_lst
    
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        import copy
        res_lst:list[list[int]] = []
        is_used:list[int] = [0] * len(nums)
        res_set = set()
        cur_res:list[int] = []
        
        def DFS(cur_res:list[int]) ->None:
            nonlocal is_used, res_lst
            if len(cur_res) == len(is_used):
                res_set.add(tuple(cur_res))
                return
            
            for i in range(len(is_used)):
                if is_used[i] == 0:
                    is_used[i] = 1
                    cur_res.append(nums[i])
                    DFS(cur_res)
                    cur_res.pop()
                    is_used[i] = 0
        
        DFS(cur_res)
        
        for elem in res_set:
            res_lst.append(list(elem))
        return res_lst        
 
    

sol = Solution()
nums = [1,1,2]
print(sol.permuteUnique(nums))
        
        
        
        
        
        
        
        