class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(n)
        exp = 0
        res = 0
        for i in range(len(n)-1, -1, -1):
            res += int(n[i]) * (2 ** exp)
            exp += 1
        # print(res)
        return res
            
        pass
    
sol = Solution()

n = 11111111111111111111111111111101
print(sol.reverseBits(n))


