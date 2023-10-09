class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        demo=set()
        for i in nums:
            if i in demo:
                return True
            else:
                demo.add(i)
       