class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if dict.get(num) != None:
                 return True;
            dict[num] = 1;
        return False;