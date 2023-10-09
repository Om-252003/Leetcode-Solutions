class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        
        return [[matrix[y][x] for y in range(len(matrix))] for x in range(len(matrix[0]))]