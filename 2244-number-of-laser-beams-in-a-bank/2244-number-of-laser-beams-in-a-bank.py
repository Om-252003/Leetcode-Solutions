class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        return (dev:=[row.count('1') for row in bank if row.count('1')]) and sum(x*y for x, y in zip(dev[1:], dev[:-1])) or 0