class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        nums_sorted.append(-1.5)
        for i in range(len(nums)):
            if nums_sorted[i-1] != nums_sorted[i] and nums_sorted[i] != nums_sorted[i+1]:
                return nums_sorted[i]