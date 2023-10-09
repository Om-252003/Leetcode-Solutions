class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        demo=[]

        for num in nums:
            demo.append(num*num)

        demo.sort()
        return demo