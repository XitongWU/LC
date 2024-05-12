class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        res = 1
        while (1):
            if res * res > x:
                while (res * res > x):
                    res -= 1
                return res
            res *= 2
        
        return 0
    
    def mySqrt1(self, x:int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        left = 1
        right = x
        
        while (left <= right):
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid == x:
                return mid
            else:
                left = mid + 1
        # print(left)
        # print(right)
        # if left * left > x:
        #     left -= 1
        return left - 1
    
    
    
sol = Solution()
x = 8
print(sol.mySqrt1(x))
# print(sol.mySqrt(x))