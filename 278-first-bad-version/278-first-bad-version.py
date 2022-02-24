# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # version = list(range(1, n + 1))
        left = 1
        right = n
        while left <= right:
            mid = (left + right)//2
            if not isBadVersion(mid):
                left=mid+1
            else:
                right=mid-1
        return left