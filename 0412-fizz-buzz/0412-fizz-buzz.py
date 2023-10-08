class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer=[]
        for i in range(1,n+1):
            if i % 3 != 0 and i % 5 != 0:
                answer.insert(i, str(i))
            elif i % 3 == 0 and i % 5 == 0:
                answer.insert(i, "FizzBuzz")
            elif i % 3 == 0:
                answer.insert(i, "Fizz")
            elif i % 5 == 0:
                answer.insert(i, "Buzz")

        return answer

        