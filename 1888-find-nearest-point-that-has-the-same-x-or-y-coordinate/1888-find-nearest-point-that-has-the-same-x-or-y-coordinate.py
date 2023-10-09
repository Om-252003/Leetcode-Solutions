class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """

        ind = -1
        dist = float('inf')
        for i, point in enumerate(points):
            if (x == point[0] or y == point[1]):
                d = abs(x-point[0]) + abs(y-point[1])
                if d < dist:
                    dist = d
                    ind = i
                        
                if dist == 0:
                    break
                
        return ind