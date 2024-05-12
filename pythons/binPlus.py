class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenA = len(a)
        lenB = len(b)
        deviation:str = abs(lenA - lenB) * '0'
        if lenA > lenB:
            b = deviation + b
        else:
            a = deviation + a
        
        # print(a)
        # print(b)
        res = []
        prog = 0
        for i in range(len(a)-1, -1, -1):
            sum = prog + int(a[i]) + int(b[i])
            if sum >= 2:
                prog = 1
                sum = sum % 2
            else:
                prog = 0
            res.append(sum)
        
        if prog == 1:
            res.append(1)
        res_str = ''
        for i in range(len(res)-1, -1, -1):
            res_str += str(res[i])
                    
        return res_str
    
    

a = '1001'
b = '1101'
sol = Solution()
print(sol.addBinary(a,b))