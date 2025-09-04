from collections import Counter

# 1. Counter-based solution
def find_duplicates_counter(nums):
    print("Using Counter:")
    counter = Counter(nums)
    print("Frequency count:", counter)
    return [num for num, count in counter.items() if count > 1]


# 2. Set-based solution
def find_duplicates_set(nums):
    print("Using Set:")
    seen = set()
    duplicates = set()
    for num in nums:
        print(f"Checking: {num}")
        if num in seen:
            print(f"Duplicate found: {num}")
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)


# 3. Sorting-based solution
def find_duplicates_sorting(nums):
    print("Using Sorting:")
    nums_sorted = sorted(nums)
    print("Sorted nums:", nums_sorted)
    duplicates = set()
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i - 1]:
            print(f"Duplicate found: {nums_sorted[i]}")
            duplicates.add(nums_sorted[i])
    return list(duplicates)


# 4. In-place marking solution (works only if nums[i] ∈ [1, n])
def find_duplicates_inplace(nums):
    print("Using In-place marking:")
    res = []
    for i in range(len(nums)):
        val = abs(nums[i])
        index = val - 1
        print(f"Index to mark: {index}, Value at index: {nums[index]}")
        if nums[index] < 0:
            print(f"Duplicate found: {val}")
            res.append(val)
        else:
            nums[index] *= -1
    return res


# Main test driver
if __name__ == "__main__":
    test_input = [4, 3, 2, 7, 8, 2, 3, 1]
    #
    # print("Original Input:", test_input)
    #
    # print("\n1. Counter-based:")
    # print(find_duplicates_counter(test_input))
    #
    # print("\n2. Set-based:")
    # print(find_duplicates_set(test_input))
    #
    # print("\n3. Sorting-based:")
    # print(find_duplicates_sorting(test_input))

    print("\n4. In-place marking:")
    input_copy = test_input.copy()  # Needed because this method modifies the input
    print(find_duplicates_inplace(input_copy))
