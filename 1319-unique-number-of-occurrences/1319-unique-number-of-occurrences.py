class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        nums = []
        occurences = []
        for num in arr:
            if num not in nums:
                occurence = arr.count(num)
                if occurence not in occurences:
                    occurences += [occurence]
                    nums += [num]
                else:
                    return False
        return True