class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=1
        for i in nums:
            if i<0:
                p*=-1
            elif i==0:
                p*=0
        return p