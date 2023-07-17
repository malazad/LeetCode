class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 1
        right = x
        
        while left <= right:
            mid = int((left + right) // 2)
            if (mid*mid) == x:
                return mid
            elif (mid * mid) < x and ((mid+1) * (mid+1)) > x:
                return mid
            elif (mid * mid) > x:
                right = mid-1
            else:
                left = mid + 1
            