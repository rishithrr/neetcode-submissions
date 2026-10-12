class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = defaultdict(list)
        for w in strs:
            k = []
            for c in w:
                k.append(abs(ord('a') - ord(c)))
            dt[tuple(sorted(k))].append(w)
        return list(dt.values())