from collections import Counter


def return_missing_balanced_numbers(elements):
    # Step 1: Count each element
    counts = Counter(elements)

    # Step 2: Find the maximum frequency
    max_count = max(counts.values())

    # Step 3: Build result dict for missing counts
    result = {}
    for elem, count in counts.items():
        if count < max_count:
            result[elem] = max_count - count

    return result


# Example tests
print(return_missing_balanced_numbers(["a", "b", "abc", "c", "a"]))
# {'b': 1, 'abc': 1, 'c': 1}

print(return_missing_balanced_numbers([1, 3, 4, 2, 1, 4, 1]))
# {2: 2, 3: 2, 4: 1}

print(return_missing_balanced_numbers([4, 5, 11, 5, 6, 11]))
# {4: 2, 6: 1}
