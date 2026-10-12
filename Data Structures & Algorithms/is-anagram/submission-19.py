class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = {}, {}
        for i in s:
            dict_s[i] = dict_s.get(i, 0) + 1
        for v in t:
            dict_t[v] = dict_t.get(v, 0) + 1
        return dict_s == dict_t