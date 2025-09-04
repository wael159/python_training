"""
Main Question: mismatched_words
------------------------------------------------------------
(Describe the main problem based on the original function.)
------------------------------------------------------------

Follow-up 1:
    (Add a variation or constraint and solve it.)

Follow-up 2:
    (Add another twist or optimize.)

Discussion:
    - Time complexity
    - Space complexity
    - Real-world use case
    - Edge cases

Advanced:
    (Optional: Extend function to handle streaming, nested data, etc.)
"""

from collections import Counter

# -------------------------------
# Main Function: Simple Comparison
# -------------------------------
def mismatched_words_main():
    sentence1 = "apple banana mango"
    sentence2 = "banana mango peach"

    words1 = sentence1.split()
    words2 = sentence2.split()

    # Words that appear in only one of the sentences
    mismatched = []
    for word in words1:
        if word not in words2:
            mismatched.append(word)
    for word in words2:
        if word not in words1:
            mismatched.append(word)

    return sorted(mismatched)


# -------------------------------
# Follow-up 1: Case-insensitive
# -------------------------------
def mismatched_words_followup1():
    sentence1 = "Apple banana Mango"
    sentence2 = "banana mango Peach"

    map1 = {word.lower(): word for word in sentence1.split()}
    map2 = {word.lower(): word for word in sentence2.split()}

    keys1 = set(map1.keys())
    keys2 = set(map2.keys())

    result_keys = keys1 ^ keys2  # symmetric difference
    result_words = []
    for word in result_keys:
        if word in map1:
            result_words.append(map1[word])
        if word in map2:
            result_words.append(map2[word])

    return sorted(result_words, key=lambda x: x.lower())


# -------------------------------
# Follow-up 2: Count differences
# -------------------------------
def mismatched_words_followup2():
    sentence1 = "apple banana mango banana"
    sentence2 = "banana mango peach banana"

    words1 = sentence1.lower().split()
    words2 = sentence2.lower().split()

    count1 = Counter(words1)
    count2 = Counter(words2)

    all_words = set(count1) | set(count2)
    mismatched = []

    for word in all_words:
        if count1[word] != count2[word]:
            mismatched.append(word)

    return sorted(mismatched)


# -------------------------------
# Test Runner
# -------------------------------
if __name__ == "__main__":
    # print("Main Function:")
    # print(mismatched_words_main())       # ➤ ['apple', 'peach']
    #
    # print("\nFollow-up 1:")
    # print(mismatched_words_followup1())  # ➤ ['Apple', 'Peach']
    #
    print("\nFollow-up 2:")
    print(mismatched_words_followup2())  # ➤ ['apple', 'peach']
