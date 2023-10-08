class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.reverse()
        s=set(nums)

        if len(s)<3:
            return max(s)
        if len(s) == 3:
            return min(s)

        else: 
            s.remove(max(s))
            s.remove(max(s))
            return max(s)