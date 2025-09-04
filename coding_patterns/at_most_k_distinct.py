from collections import defaultdict


def at_most_k_distinct(nums, k):
    if k == 0 or not nums:
        return 0

    counts = defaultdict(int)
    left = 0
    best = 0

    for right in range(len(nums)):
        # 1) expand window
        counts[nums[right]] += 1

        # 2) shrink while too many distinct
        while len(counts) > k:
            counts[nums[left]] -= 1
            if counts[nums[left]] == 0:
                del counts[nums[left]]
            left += 1

        # 3) update best
        best = max(best, right - left + 1)

    return best



def at_most_k_distinct_n2(nums, k):
    n = len(nums)
    best = 0
    for left in range(n):
        seen = set()
        for right in range(left, n):
            seen.add(nums[right])
            if len(seen) > k:
                break
            best = max(best, right - left + 1)
    return best

