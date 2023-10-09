class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxi=max(nums)

        res=nums.index(maxi)
        nums.remove(maxi)
        for n in nums:
            if n*2 > maxi: return -1
        return res