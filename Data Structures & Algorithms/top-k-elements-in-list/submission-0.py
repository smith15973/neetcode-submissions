class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for n in nums:
            if n not in frequency_map:
                frequency_map[n] = 0
            frequency_map[n] = frequency_map[n] + 1
        
        arr = []
        for key, value in frequency_map.items():
            if value >= k:
                arr.append(key)

        return arr