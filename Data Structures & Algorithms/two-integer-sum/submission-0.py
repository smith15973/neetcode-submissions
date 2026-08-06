class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hashmap = {value: index for index, value in enumerate(nums)}

        for key in my_hashmap:
            goal = target - key

            if goal != key and goal in my_hashmap:
                return[my_hashmap[key], my_hashmap[goal]]