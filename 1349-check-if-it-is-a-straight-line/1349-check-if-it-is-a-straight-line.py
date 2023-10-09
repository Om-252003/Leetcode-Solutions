class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates)<3:
            return True
        
        (x0,y0),(x1,y1)=coordinates[:2]

        for i,j in coordinates:
            if (y1-y0)*(i-x0)!=(j-y0)*(x1-x0):
                return False
        return True