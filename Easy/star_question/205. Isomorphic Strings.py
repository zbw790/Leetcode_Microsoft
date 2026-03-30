class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #直接用两个map跟踪
        letter_map_1 = {}
        letter_map_2 = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in letter_map_1 and t[i] not in letter_map_2:
                letter_map_1[s[i]] = t[i]
                letter_map_2[t[i]] = s[i]
            elif s[i] in letter_map_1 and t[i] in letter_map_2 and letter_map_1[s[i]] == t[i]:
                pass
            else:
                return False

        return True