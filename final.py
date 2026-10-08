class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2
            parts = 1
            cur = 0

            for x in nums:
                if cur + x > mid:
                    parts += 1
                    cur = x
                else:
                    cur += x

            if parts <= k:
                right = mid
            else:
                left = mid + 1

        return left
