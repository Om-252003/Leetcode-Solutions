class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            x = x+1 if ("+" in op) else x-1
        return x