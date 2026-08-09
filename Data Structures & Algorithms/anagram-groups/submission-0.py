class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_dict = {}

        for index, s in enumerate(strs):
            sorted_s = ''.join(sorted(s))
            if sorted_s not in s_dict:
                s_dict[sorted_s] = []
            s_dict[sorted_s].append(index)

        arr = []
        for key, values in s_dict.items():
            arr.append([strs[i] for i in values])
        
        return arr
        

        


