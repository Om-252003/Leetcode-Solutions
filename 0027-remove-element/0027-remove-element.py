class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        for i in range(0,(len(nums)+1)):
            if val in nums:
                nums.remove(val)

        length=len(nums)
        return length