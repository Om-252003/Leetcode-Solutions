class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """

        ans = []
        diff = (sum(bobSizes) - sum(aliceSizes)) / 2
        setAliceSizes = set(aliceSizes)
        for bobItem in bobSizes:
            if bobItem - diff in setAliceSizes:
                ans.append(int(bobItem - diff))
                ans.append(bobItem)
                return ans
        return ans