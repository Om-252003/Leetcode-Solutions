class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i*2-n+1 for i in range(0,n)]