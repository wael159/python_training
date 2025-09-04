from collections import Counter

# ------------------------------------------------------------
# Main Question: Find all starting indices of permutations of S in B
# ------------------------------------------------------------
def find_permutation_indices(S, B):
    len_s, len_b = len(S), len(B)
    if len_s > len_b:
        return []

    s_count = Counter(S)
    window_count = Counter(B[:len_s])
    result = []

    if window_count == s_count:
        result.append(0)

    for i in range(len_s, len_b):
        start_char = B[i - len_s]
        end_char = B[i]

        window_count[end_char] += 1
        window_count[start_char] -= 1

        if window_count[start_char] == 0:
            del window_count[start_char]

        if window_count == s_count:
            result.append(i - len_s + 1)

    return result

# ------------------------------------------------------------
# Follow-up 1: Return the substrings, not just the indices
# ------------------------------------------------------------
def find_permutation_substrings(S, B):
    indices = find_permutation_indices(S, B)
    return [B[i:i+len(S)] for i in indices]

# ------------------------------------------------------------
# Follow-up 2: Case-insensitive match
# ------------------------------------------------------------
def find_permutation_indices_case_insensitive(S, B):
    return find_permutation_indices(S.lower(), B.lower())

# ------------------------------------------------------------
# Tests
# ------------------------------------------------------------
def run_tests():
    print("Running tests...")

    S = "abc"
    B = "cbabcacab"
    print("Test 1 - Indices:", find_permutation_indices(S, B))  # [0, 2, 5]
    print("Test 2 - Substrings:", find_permutation_substrings(S, B))  # ['cba', 'abc', 'cab']

    # S2 = "AbC"
    # B2 = "XcbaabcCABz"
    # print("Test 3 - Case-insensitive indices:", find_permutation_indices_case_insensitive(S2, B2))  # [1, 4, 7]
    #
    # S3 = "xyz"
    # B3 = "abcdefg"
    # print("Test 4 - No match:", find_permutation_indices(S3, B3))  # []
    #
    # S4 = "abc"
    # B4 = "ab"
    # print("Test 5 - Pattern longer than text:", find_permutation_indices(S4, B4))  # []
    #
    # print("All tests completed.")

if __name__ == "__main__":
    run_tests()
