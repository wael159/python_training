def contains_duplicate(nums):
    seen = set()  # Step 1: store numbers we've seen so far

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
# Step 2: check if num already in seen

# Step 3: otherwise, add num to seen

# Step 4: no duplicates found
