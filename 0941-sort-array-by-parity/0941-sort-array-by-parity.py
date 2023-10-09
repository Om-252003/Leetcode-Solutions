class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        demo = list()

        for no in nums:
            if no %2 == 0:
                demo.append(no)

        for no in nums:
            if no %2 != 0:
                demo.append(no)

        return demo