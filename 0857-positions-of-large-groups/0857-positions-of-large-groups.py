class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """

        i, j, N = 0, 0, len(s)
        res = []
        while i < N:
            while j < N and s[j] == s[i]: j += 1
            if j - i >= 3: res.append([i, j - 1])
            i = j
        return res