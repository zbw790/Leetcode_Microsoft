class Solution:
    def isValid(self, s: str) -> bool:
        tempList = []
        openBracketList = ["(", "{", "["]
        bracket_map = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }

        if s == "":
            return True
        elif len(s) % 2 == 1:
            return False

        for i in range(len(s)):
            if s[i] in openBracketList:
                tempList.append(s[i])
            elif tempList != [] and s[i] == bracket_map[tempList[-1]]:
                tempList.pop()
            else:
                return False
        
        return tempList == []