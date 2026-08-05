class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = None
        my_dict = {}
        for index, num in enumerate(nums):
            my_dict[index] = num;
        
        for index, num in enumerate(nums):
            goal = target-num
            if goal in my_dict.values():
                i = index
        
        for index, num in enumerate(nums):
            if (nums[i] + num) == target:
                return [index, i]
                