class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res = s = 0
        for v in gain:
            s += v
            res = max(res, s)
        return res