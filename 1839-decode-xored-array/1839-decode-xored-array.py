class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        n = len(encoded)
        arr = [0]*(n+1)
        arr[0] = first
        for i in range(n):
            arr[i+1] = (encoded[i] ^ arr[i])
        return arr