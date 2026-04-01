class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        final_combinations = []

        def backtrack(i, path):
            if len(path) == len(digits):
                final_combinations.append("".join(path))
                return None
            
            possible_choice = number_letter_map[digits[i]]
            for char in possible_choice:
                path.append(char)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return final_combinations

        

