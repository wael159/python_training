def return_mismatched_words(str1, str2):
    words1 = str1.split()
    words2 = str2.split()

    # Mismatched: in one list but not the other
    result = [w for w in words1 if w not in words2]
    result += [w for w in words2 if w not in words1]

    return result


# Example
print(return_mismatched_words("firstly this is the first string",
                              "Next is the second string"))
# Expected: ['firstly', 'this', 'first', 'Next', 'second']
