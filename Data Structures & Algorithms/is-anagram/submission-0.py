from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        count_in_s = defaultdict(int)
        count_in_t = defaultdict(int)
        for z in s :
            count_in_s[z] += 1
        for y in t :
            count_in_t[y] += 1
        set_s = set(s)
        for a in set_s :
            if count_in_t[a] != count_in_s[a] :
                return False
        return True
        