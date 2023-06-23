class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_dict = {}
        mapped_letters = set()
        for i in range(len(s)):
            try:
                if letter_dict[s[i]] != t[i]:
                    return False
            except KeyError:
                if t[i] in mapped_letters:
                    return False
                letter_dict.update({s[i] : t[i]})
                mapped_letters.add(t[i])
        return True