import re
import collections

def is_anagram(a, b):
    clean_a = re.sub('[^A-Za-z0-9]','',a)
    clean_a=clean_a.lower()
    clean_b = re.sub('[^A-Za-z0-9]','',b)
    clean_b=clean_b.lower()
# Step 1: normalize both strings (lowercase + remove non-alphanumeric)
    count_a = collections.Counter(clean_a,0)
    count_b = collections.Counter(clean_b,0)
    return count_a == count_b



import re

def is_anagram_2(a, b):
    # Step 1: normalize
    clean_a = re.sub('[^A-Za-z0-9]', '', a).lower()
    clean_b = re.sub('[^A-Za-z0-9]', '', b).lower()

    # Step 2: if lengths differ → not an anagram
    if len(clean_a) != len(clean_b):
        return False

    # Step 3: build frequency dict for clean_a
    count_a = {}
    for ch in clean_a:
        count_a[ch] = count_a.get(ch, 0) + 1

    # Step 4: build frequency dict for clean_b
    count_b = {}
    for ch in clean_b:
        count_b[ch] = count_b.get(ch, 0) + 1

    # Step 5: compare
    return count_a == count_b

import re

def is_anagram_3(a, b):
    # Step 1: normalize
    clean_a = re.sub('[^A-Za-z0-9]', '', a).lower()
    clean_b = re.sub('[^A-Za-z0-9]', '', b).lower()

    # Step 2: quick length check
    if len(clean_a) != len(clean_b):
        return False

    # Step 3: single dict counting
    counts = {}
    for ch in clean_a:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in clean_b:
        counts[ch] = counts.get(ch, 0) - 1

    # Step 4: all counts must be zero
    for val in counts.values():
        if val != 0:
            return False
    return True

