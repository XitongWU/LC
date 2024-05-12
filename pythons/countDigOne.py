class Solution:
    def countDigitOne(self, n: int) -> int:
        
        def getDig(n:int)->int:
            sum = 0
            while n > 0:
                cur_dig = n%10
                if cur_dig == 1:
                    sum += 1
                n -= cur_dig
                n //= 10
            return sum
        
        count = 0
        for i in range(0, n + 1):
            count += getDig(i)
        
        return count
    

sol = Solution()
n = 13
print(sol.countDigitOne(n))