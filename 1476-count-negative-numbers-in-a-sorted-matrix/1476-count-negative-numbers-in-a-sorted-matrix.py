class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s=[]
        demo = []
        for i in grid:
             for j in i: s.append(j)

        for i in s:
             if i < 0: demo.append(i)
        return len(demo)      