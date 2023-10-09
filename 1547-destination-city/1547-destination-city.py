class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        source = set()
        dest = set()
        for l in paths:
            source.add(l[0])
            dest.add(l[1])
        return list(dest - source)[0]