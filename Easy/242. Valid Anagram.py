class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        letter_map = {}
        for char in s:
            if char in letter_map:
                letter_map[char] += 1
            else:
                letter_map[char] = 1
        
        for char in t:
            if char in letter_map and letter_map[char] > 0:
                letter_map[char] -= 1
            else:
                return False

        return True