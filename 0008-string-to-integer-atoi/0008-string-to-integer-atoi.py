class Solution:
    def myAtoi(self, s: str) -> int:

        temp = s.strip()
        print(temp)
        sign=1
        ans=0
        isindexMoreThanOne=0

        for i in temp:

            if i == '-' and isindexMoreThanOne == 0:
                isindexMoreThanOne = 1
                sign = -1
                continue
            if i == '+' and isindexMoreThanOne==0: 
                isindexMoreThanOne = 1
                continue
            if not i.isdigit(): break
            if i.isdigit():
                ans=(ans*10)+int(i)
                isindexMoreThanOne = 1

            if ans*sign <( (-2) ** 31):
                ans = 2 ** 31
                break

            if ans*sign  > ((2 ** 31) - 1):
                ans = (2 ** 31) - 1
                break


        return ans*sign
