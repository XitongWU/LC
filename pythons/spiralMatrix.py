class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []

        result = []
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
    
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
                
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
            
            
            
    def generateMatrix(self, n: int) -> list[list[int]]:
        
        if n == 1:
            return [[1]]
        
        import copy
        matrix = []
        
        for i in range(0,n):
            cur_row = []
            for j in range(n):
                cur_row.append(0)
            matrix.append(copy.deepcopy(cur_row))

        top, bottom, left, right = 0, n - 1, 0, n - 1
        val = 1
        
        while top <= bottom and left <= right:
            
            for i in range(left, right + 1):
                matrix[top][i] = val
                val += 1
            top += 1

            for i in range(top, bottom + 1):
                matrix[i][right] = val
                val += 1
            right -= 1
            
            if top <= bottom:
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = val
                    val += 1
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = val
                    val += 1
                left += 1
            
        return matrix
        
        
        
        
        
        
        pass
            
        
sol = Solution()
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# print(sol.spiralOrder(matrix))

print(sol.generateMatrix(3))