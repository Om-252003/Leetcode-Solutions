class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        v1, v2 = cost[-2], cost[-1]
        for i in range(len(cost) - 3, -1, -1):
             v1, v2 = min(v1, v2) + cost[i], v1
        
        return min(v1, v2)