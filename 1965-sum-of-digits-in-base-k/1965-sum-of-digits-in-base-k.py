class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        demo=0
        while n>0: demo+=n%k ; n//=k
        return demo