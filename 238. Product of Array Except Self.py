class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] not in hashmap.keys():
                product = 1
                for j in range(i):
                    product = product * nums[j]
                for j in range(i+1, len(nums)):
                    product = product * nums[j]
                    
                hashmap[nums[i]] = product
        answer = []
        for num in nums:
            answer.append(hashmap[num])
        return answer