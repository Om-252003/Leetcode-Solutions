class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        ret = True
        for bit in bits[-2::-1]:
            if bit: ret = not ret
            else: break
        return ret