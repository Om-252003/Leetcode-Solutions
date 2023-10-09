class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [list(str(bin(i))).count("1") for i in range(0, n + 1)]