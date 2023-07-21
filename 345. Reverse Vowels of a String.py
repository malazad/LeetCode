class Solution:
    def reverseVowels(self, s: str) -> str:
        
        indexList = []
        vowelList = []
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

        for i in range(len(s)):
            if s[i] in vowels:
                indexList.append(i)
                vowelList.insert(0,s[i])
        s = list(s)
        for i in range(len(indexList)):
            s[indexList[i]] =  vowelList[i]
        return ''.join(s)