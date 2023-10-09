class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        if n==1: return 1 
        s, d = set(list(range(1, n+1))), defaultdict(lambda:0) 
        for p1, p2 in trust:
            if p1 in s: 
                s.remove(p1)
            d[p2] += 1
        for p in s:
            if p in d and d[p]==n-1:
                return p
        return -1