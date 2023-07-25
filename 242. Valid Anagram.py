class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        length = len(s)
        s_letters = []
        s_letters_frq = []
        t_letters = []
        t_letters_frq = []

        for i in range(length):
            if s[i] not in s_letters:
                s_letters.append(s[i])
                s_letters_frq.append(1)
            else:
                s_letters_frq[s_letters.index(s[i])] += 1
            if t[i] not in t_letters:
                t_letters.append(t[i])
                t_letters_frq.append(1)
            else:
                t_letters_frq[t_letters.index(t[i])] += 1
            
        if len(s_letters) != len(t_letters):
            return False
        for i in range(len(s_letters)):
            if s_letters[i] not in t_letters:
                return False
            index = t_letters.index(s_letters[i])
            if s_letters_frq[i] != t_letters_frq[index]:
                return False
        return True
