class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        prev = ''
        i = 0

        for c in typed:
            if i < len(name) and c == name[i]:
                i += 1
                prev = c
                continue

            if c != prev:
                return False

        return i == len(name)
