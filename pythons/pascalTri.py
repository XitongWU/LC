class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        
        res = [[1],[1,1]]
        for i in range(2, numRows):
            this_row = [1]
            for j in range(1, i):
                this_row.append(res[i-1][j-1] + res[i-1][j])
            this_row.append(1)
            res.append(this_row)
            
        return res
    
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        
        res = [[1],[1,1]]
        for i in range(2, rowIndex + 1):
            this_row = [1]
            for j in range(1, i):
                this_row.append(res[i-1][j-1] + res[i-1][j])
            this_row.append(1)
            res.append(this_row)
            
        return res[rowIndex]
        pass
    
sol = Solution()
n = 5
print(sol.generate(n))