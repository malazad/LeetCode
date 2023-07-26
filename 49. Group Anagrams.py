    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in hashmap.keys():
                hashmap[str(s_sorted)] = []
            hashmap[s_sorted] += [s]
        return list(hashmap.values())
