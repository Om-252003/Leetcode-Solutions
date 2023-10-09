class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        if len(path) < 2: return False
        passed = set()
        passed.add((0, 0))
        x, y = 0, 0
        for i in path: 
            if i == 'N': y += 1
            elif i == 'S': y -= 1
            elif i == 'E': x += 1
            elif i == 'W': x -= 1
            currentPoint = (x, y)
            if currentPoint in passed: return True
            passed.add(currentPoint)
        return False