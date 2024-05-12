class Solution:
    def isValid(self, s: str) -> bool:
        sLst = []
        stack = []
        for char in s:
            sLst.append(char)
            
        while sLst:
            top = sLst.pop()
            if top == '}' or top == ']' or top == ')':
                stack.append(top)
            else:
                if len(stack) == 0:
                    return False
                else:
                    stack_top = stack.pop()
                    if stack_top == ')' and top == '(':
                        continue
                    elif stack_top == ']' and top == '[':
                        continue
                    elif stack_top == '}' and top == '{':
                        continue
                    else:
                        return False
                    
        if len(stack) == 0:
            return True
        else:
            return False
        
    def removeElement(self, nums: list[int], val: int) -> int:
        inf = 9999999

        cur_length = len(nums)

        if len(nums) == 0:
            return nums
        for i in range(0, len(nums)):
            if nums[i] == val:
                nums[i] += inf
                cur_length -= 1
                
        # print(nums)
        nums.sort()
        # print(nums)
        return cur_length
        
    
    
sol = Solution()
inp = '()({)}'
# print(sol.isValid(inp))

lst = [0,1,2,2,3,0,4,2]
val = 2
sol.removeElement(lst, val)