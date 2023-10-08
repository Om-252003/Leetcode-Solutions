class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        demo=set(nums)
        nums2=[]

        for i in range(1,len(nums)+1):
            if i in demo:
                demo.remove(i)
            else :
                nums2.append(i)
        return nums2