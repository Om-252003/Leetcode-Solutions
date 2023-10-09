class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        demo = []
        for i in operations:
            if i == "C":
                demo.pop()
                
            elif i == "D":
                demo.append(demo[-1]*2)

            elif i == "+":
                demo.append(demo[-1]+demo[-2])

            else: demo.append(int(i))

        return sum(demo)
        