class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        s="aceg"
        if coordinates[0] in s:
            return int(coordinates[1])%2==0
        return int(coordinates[1])%2!=0