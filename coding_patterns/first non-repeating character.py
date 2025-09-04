from collections import Counter

def first_unique_char(s):
    # Step 1: count characters
    count_char = Counter(s)

    # Step 2: loop over string with index and char
    for idx, ch in enumerate(s):
        if count_char[ch] == 1:   # Step 3
            return idx

    return -1  # Step 4



def first_unique_char_2(s):
    counts = {}

    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for idx,ch in enumerate(s):
        if counts[ch] == 1:
            return idx
    return -1


def first_unique_char_3(s):
    counts = [0] * 26  # one slot per lowercase letter
    for ch in s:
        counts[ord(ch) - ord('a')] += 1

    for idx, ch in enumerate(s):
        if counts[ord(ch) - ord('a')] == 1:
            return idx
    return -1
