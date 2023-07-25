class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        string_dict = {len(s): [] for s in strs}
        for s in strs:
            string_dict[len(s)].append(s)

        for x in string_dict:
            strs = string_dict[x]
            while len(strs) > 0:
                temp_anagram_list = []
                temp_anagram_list.append(strs[0])
                pop_list = []
                for i in range(1,len(strs)):
                    if len(strs[0]) == len(strs[i]):
                        if self.isAnagram(strs[0], strs[i]):
                            temp_anagram_list.append(strs[i])
                            pop_list.append(i)
                for i in range(len(pop_list)-1, -1, -1):
                    strs.pop(pop_list[i])
                strs.pop(0)
                final_list.append(temp_anagram_list)
        return final_list
