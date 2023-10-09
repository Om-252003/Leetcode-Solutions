class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_backspaced = []
        t_backspaced = []
        
        for i in range(len(s)):
            if s[i] == '#':
                if s_backspaced:
                    s_backspaced.pop()
            else:
                s_backspaced.append(s[i])
            
        for i in range(len(t)):
            if t[i] == '#':
                if t_backspaced:
                    t_backspaced.pop()
            else:
                t_backspaced.append(t[i])
        
        return s_backspaced == t_backspaced