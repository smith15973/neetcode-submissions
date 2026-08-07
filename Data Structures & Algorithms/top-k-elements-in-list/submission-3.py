class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            freq_map[n] = 1+ freq_map.get(n, 0)
        for n, count in freq_map.items():
            freq[count].append(n)
        
        arr = []
        for i in range(len(freq) - 1, 0, -1):
            arr.extend(freq[i])
            if (len(arr) >= k):
                return arr

            