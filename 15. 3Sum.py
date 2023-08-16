class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        valid_triplets = []
        for start in range(len(nums)):
            left = start + 1
            right = len(nums) - 1
            target = 0 - nums[start]
            while left < right:
                if  nums[left] + nums[right] == target:
                    if [nums[left], nums[start], nums[right]] not in valid_triplets:
                        valid_triplets.append([nums[left], nums[start], nums[right]])
                    left += 1
                elif  nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return valid_triplets