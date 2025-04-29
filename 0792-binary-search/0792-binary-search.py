class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.bs(nums, 0, len(nums)-1, target)

    def bs(self, nums, start, end, target):
        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.bs(nums, mid+1, end, target)
        else:
            return self.bs(nums, start, mid-1, target)
