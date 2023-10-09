class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) != 1:
            stones.sort()
            a, b = stones.pop(), stones.pop()
            stones.append(a-b)
           
        return stones[0]