class Solution:
    # def myPow(self, x, n):
    #     if n == 0:
    #         return 1
    #     if n == 1:
    #         return x
    #     if n < 0:
    #         x = 1 / x
    #         n = -n
        
    #     half = self.myPow(x, n // 2)
    #     if n % 2 == 0:
    #         return half * half
    #     else:
    #         return half * half * x
        
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        def pow(x: float, n: int):
            if n == 1:
                return x

            half = pow(x, n // 2)

            if n % 2 != 0:
                return half * half * x
            else:
                return half * half
        
        result = pow(x, abs(n))
        if n < 0:
            return 1 / result
        else:
            return result
        
sol = Solution()
x = 10
n = 3
print(sol.myPow(x, n))