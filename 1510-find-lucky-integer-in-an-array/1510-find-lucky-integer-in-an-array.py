class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s=set()

        for i in arr:
            if i == arr.count(i):
                s.add(i)

        if len(s) > 0: return max(s)
        else : return -1