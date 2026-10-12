class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i, v in enumerate(s):
            s_dict[v] = 1 + s_dict.get(v, 0)
        t_dict = {}
        for i, v in enumerate(t):
            t_dict[v] = 1 + t_dict.get(v, 0)
        return  s_dict == t_dict
        
        