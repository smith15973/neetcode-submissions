class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for n in nums:
            if n not in frequency_map:
                frequency_map[n] = 0
            frequency_map[n] = frequency_map[n] + 1
        
        arr = sorted(frequency_map.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in arr[:k]]