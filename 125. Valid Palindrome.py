class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        ap = ''
        for i in range(len(s)):
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9'):
                print(s[i])
                ap = ap + s[i]
                
        s = ap
        i = 0 
        j = len(s) -1

        while i <=j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True