from collections import defaultdict


def group_anagrams(words):
    groups = defaultdict(list)  # Step 1: map sorted word -> list of words

    for word in words:
        sorted_word = tuple(sorted(word))
        groups[sorted_word].append(word)

    return list(groups.values())
# Step 2: sort the word to get the key

# Step 3: append the original word to the right group

# Step 4: return all the grouped lists
