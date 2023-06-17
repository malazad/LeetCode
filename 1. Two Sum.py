class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(len(nums)):
            y = target - nums[index1]
            if y != nums[index1]:
                if y in nums:
                    index2 = nums.index(y)
                    return [index1, index2]
            else:
                nums[index1] = y + 1
                if y in nums:
                    index2 = nums.index(y)
                    return [index1, index2] 
                nums[index1] = y