class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = 0
        index2 = 0
        while index2 < n:
            while True:
                if nums1[index1] == 0 and max(nums1[index1:]) == 0:
                    for i in range(index2, len(nums2)):
                        nums1.insert(index1, nums2[i])
                        index1+=1
                    break
                if nums1[index1] == nums2[index2] or nums1[index1] > nums2[index2]:
                    nums1.insert(index1, nums2[index2])
                    index1 += 1
                    break
                index1 += 1
            index2 += 1
        del nums1[m+n:]