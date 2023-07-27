class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for num in nums:
            if num not in hashmap.keys():
                hashmap[num] = 0
            hashmap[num] += 1
        hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        print(hashmap)
        return list(dict(list(hashmap.items())[:k]).keys())