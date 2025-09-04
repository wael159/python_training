def rotate_array(nums, k):
    n = len(nums)
    if n == 0:
        return  # nothing to do

    k %= n  # handle k > n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]  # swap
            start += 1
            end -= 1

    # Step 1: reverse the whole array
    reverse(0, n - 1)

    # Step 2: reverse the first k elements
    reverse(0, k - 1)

    # Step 3: reverse the remaining n-k elements
    reverse(k, n - 1)



def rotate_array(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k %= n
    return nums[-k:] + nums[:-k]
