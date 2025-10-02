class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        numEmpty = numBottles

        while numEmpty >= numExchange:
            res += 1
            numEmpty -= numExchange - 1
            numExchange += 1
        
        return res