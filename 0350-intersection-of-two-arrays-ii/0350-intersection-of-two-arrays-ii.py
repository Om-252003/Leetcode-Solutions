class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        list3=[]

        for num in nums1:
            if num in nums2:
                list3.append(num)
                nums2.remove(num)
        return list3