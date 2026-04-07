class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp_1 = {i: s.count(i) for i in set(s)}
        mp_2 = {i: t.count(i) for i in set(t)}

        if len(s)!=len(t) or mp_1!=mp_2:
            return False
        else:
            return True