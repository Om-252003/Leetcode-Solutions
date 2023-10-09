class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        counter = defaultdict(int)
        for num in range(lowLimit, highLimit+1):
            counter[sum(map(int,str(num)))] += 1
        return max(counter.values())