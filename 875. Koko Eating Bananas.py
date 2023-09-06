class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        k= right
        while left <= right:
            mid = (left + right)//2
            count = 0
            for i in piles:
                count += ceil(i/mid)
            if count<= h:
                right = mid - 1
                k = min(k, mid)
            else:
                left = mid + 1
        return k