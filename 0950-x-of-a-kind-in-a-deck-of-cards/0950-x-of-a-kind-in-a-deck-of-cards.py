class Solution(object):

    def gcd(self, count, res):
        return self.gcd(res, count%res) if res > 0 else count

    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """


        map = {}
        result = 0
        for i in deck:
            if i in  map:
                map[i] += 1
            else:
                map[i] = 1
        for value in map.itervalues():
            result = self.gcd(value, result)
        return result > 1