class Solution(object):
    def isToeplitzMatrix(self, matrix):
        rows= len(matrix)
        cols=len(matrix[0])

        for row in range(rows-1):
            for col in range(cols-1):
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False
        return True
        
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
