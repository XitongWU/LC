class Solution:
    def isHappy(self, n: int) -> bool:
        
        res_set = set()
        res_set.add(n)
        def getSum(n:int) -> int:
            sum = 0
            while n > 0:
                cur_dig = n % 10
                sum += cur_dig ** 2
                n -= cur_dig
                n = n // 10
            return sum
        
        while(1):
            n = getSum(n)
            if n == 1:
                return True
            else:
                if n in res_set:
                    return False
                else:
                    res_set.add(n)

    
sol = Solution()
n = 2
print(sol.isHappy(n))