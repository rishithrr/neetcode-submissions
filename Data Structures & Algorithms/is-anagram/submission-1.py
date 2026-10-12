class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def freq(str):
            dict={}
            for s in range(len(str)):
                if str[s] not in dict.keys():
                    dict.update({str[s]:1})
                else:
                    i=dict.get(str[s])
                    i=i+1
                    dict.update({str[s]:i})
            return dict
        a=freq(s)
        b=freq(t)

        if a==b:
            return True
        else:
            return False
