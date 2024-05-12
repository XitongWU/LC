class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = 0
        if dividend == 0:
            return 0
        if dividend < 0:
            dividend = abs(dividend)
            neg += 1
        if divisor < 0:
            divisor = abs(divisor)
            neg += 1
        
        sum = 0
        res = 0
        while (1):
            if sum == dividend:
                break
            elif sum > dividend:
                res -= 1
                break
            else:
                sum += divisor
                res += 1
                
        if neg == 1:
            return res - res - res
        else:
            return res
        
sol = Solution()
# print(sol.divide(10, -3))

print(15//4)