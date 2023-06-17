class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if s == t:
            return True
        previous_index = -1
        temp = 0
        for x in s:
            for i in range(temp,len(t), 1):
                if x == t[i] and previous_index < i:
                    previous_index = i
                    temp = i
                    break
                if i == len(t) -1:
                    return False
        return True