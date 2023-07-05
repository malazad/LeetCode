class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[-1] == len(nums) - 1:
            return len(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            elif nums[mid] > mid and nums[mid-1] == mid - 1:
                return mid
            elif nums[mid] > mid and mid == 0:
                return mid
            elif nums[mid] > mid:
                right = mid - 1