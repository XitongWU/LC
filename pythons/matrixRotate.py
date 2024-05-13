class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1:
            return matrix
        width = len(matrix)
        for i in range(width):
            for j in range(i, width):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(width):
            for j in range(0, width // 2):
                matrix[i][j], matrix[i][width - j - 1] = matrix[i][width - j - 1], matrix[i][j]
        
        # return matrix                

        
        
sol = Solution()
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

sol.rotate(matrix)
        