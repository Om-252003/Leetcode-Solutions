class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        l1=list(bin(n))

        l1.__delitem__(0)
        l1.__delitem__(0)

        cnt,ans = 0,0

        for i in range(len(l1)):
            if l1[i] == '1':
                if cnt == 0:
                    cnt = cnt + 1

                else :
                    ans = max(ans,cnt)
                    cnt=1

            if l1[i] == '0': cnt = cnt+1

        return ans       