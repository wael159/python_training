def search_range(nums, target):
    def bound(is_left):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (is_left and nums[mid] == target):
                hi = mid
            else:
                lo = mid + 1
        return lo

    left = bound(True)
    right = bound(False) - 1

    if left <= right and 0 <= left < len(nums) and nums[left] == target:
        return (left, right)
    return (-1, -1)


