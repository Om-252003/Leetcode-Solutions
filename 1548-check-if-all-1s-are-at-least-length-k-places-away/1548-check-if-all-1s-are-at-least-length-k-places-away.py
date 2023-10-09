class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = k #'<- the cheating line
        for i in nums:
            if i == 0:
                n += 1
            else:
                if n < k:
                    return False
                n = 0
        return True