class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        sums=0
        while temp>0 :
            r = temp%10
            temp=temp//10
            sums=(sums*10) + r

            if (sums < (-2) ** 31)  or sums  > ((2 ** 31) - 1):
                return 0
                exit(123)

        if x<0:  return -sums
        return sums