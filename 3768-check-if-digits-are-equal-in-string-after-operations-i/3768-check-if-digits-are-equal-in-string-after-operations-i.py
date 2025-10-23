class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            res = ""
            for i in range(1,len(s)):
                res += str((int(s[i]) + int(s[i-1])) % 10)
            s = res
        return s[1] == s[0]