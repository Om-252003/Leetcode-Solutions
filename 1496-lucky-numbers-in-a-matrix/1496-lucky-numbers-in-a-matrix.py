class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})