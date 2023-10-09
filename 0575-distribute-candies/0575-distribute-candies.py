class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        s= set(candyType)
        minimum=min(len(candyType)//2, len(s))
        return minimum