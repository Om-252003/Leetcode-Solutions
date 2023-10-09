class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        demo=[]
        for i in nums:
            if nums.count(i)<2:
                demo.append(i)

        return sum(demo)