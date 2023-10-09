class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        answer = [''] * len(s)

        for i in xrange(len(s)):     
            target_index = indices[i]
            answer[target_index] = s[i]
        
        return ''.join(answer)