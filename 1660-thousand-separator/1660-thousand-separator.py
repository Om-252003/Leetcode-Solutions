class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = str(n)[::-1]
        res = '.'.join(res[i:i + 3] for i in range(0, len(res), 3))

        return res[::-1]