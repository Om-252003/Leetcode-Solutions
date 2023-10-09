class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        cnt=0
        for l1 in jewels:
            for l2 in stones:
                if l1 == l2 : cnt+=1

        return cnt