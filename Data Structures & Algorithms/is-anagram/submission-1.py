class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dict1 = {}
        dict2 = {}

        for l in s:
                if l in dict1:
                    dict1[l] = dict1[l] + 1
                else:
                    dict1[l] = 1
        for l in t:
                if l in dict2:
                    dict2[l] = dict2[l] + 1
                else:
                    dict2[l] = 1
        
        for key in dict1:
            if key not in dict2:
                return False
            if dict1[key] != dict2[key]:
                return False
        return True

        