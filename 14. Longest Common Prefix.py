class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ''
        if "" in strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        min_length = len(strs[0])
        min_str = strs[0]

        for s in strs:
            if len(s) <= min_length:
                min_length = len(s)
                min_str = s
        common_prefix = ''
        for i in range(len(min_str)):
            for s in strs:
                if min_str[i] != s[i]:
                    return common_prefix
            common_prefix = common_prefix + min_str[i]
        return common_prefix
        '''
        common_prefix = []
        for i in range(len(strs)):
            s = strs[i]
            substrings = []
            #for start in range(len(s)):
            for end in range(0,len(s)):
                #if s[start:end] not in substrings:
                substrings.append(s[0:end+1])
            if i == 0:
                common_prefix = substrings
            elif len(common_prefix) == 0:
                    return ''
            else:
                common_prefix = list(set(common_prefix).intersection(set(substrings)))
        if len(common_prefix) == 0:
                    return ''
        lengths = [len(s) for s in common_prefix]
        zipped_list = sorted(list(zip(lengths, common_prefix)))
        max_length = zipped_list[-1][0]
        index = -1
        for i in range(len(common_prefix)):
            if len(zipped_list[i][1]) == max_length:
                index = i
                break
        return zipped_list[index][1]
        '''
        
