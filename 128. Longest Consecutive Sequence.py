class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        hashmap = dict()
        starts = []
        for num in nums:
            if num not in hashmap.keys():
                hashmap[num] = 1
                
        for num in nums:
            if num-1 not in hashmap.keys():
                starts.append(num)
        
        max_lenth = 0
        for start in starts:
            length = 1
            num = start
            while num+1 in hashmap.keys():
                length += 1
                num += 1
            if max_lenth < length:
                max_lenth = length
        return max_lenth