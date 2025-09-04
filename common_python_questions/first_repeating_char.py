from collections import Counter

# Main function: using set (one pass)
def first_repeating_char_main():
    def first_repeating_char(s):
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)
        return None

    print(first_repeating_char("abcba"))     # Output: b
    # print(first_repeating_char("abcdef"))    # Output: None
    # print(first_repeating_char("aabbcc"))    # Output: a
    # print(first_repeating_char(""))          # Output: None
    # print(first_repeating_char("zxyxz"))     # Output: x


# Follow-up 1: case-insensitive comparison
def first_repeating_char_followup1():
    def first_repeating_char_case_insensitive(s):
        seen = set()
        for ch in s:
            ch_lower = ch.lower()
            if ch_lower in seen:
                return ch
            seen.add(ch_lower)
        return None

    print(first_repeating_char_case_insensitive("AbcBa"))  # Output: B
    print(first_repeating_char_case_insensitive("abcdef")) # Output: None
    # print(first_repeating_char_case_insensitive("aAbb"))   # Output: A
    # print(first_repeating_char_case_insensitive(""))       # Output: None


# Follow-up 2: return index of first repeating character
def first_repeating_char_followup2():
    def index_of_first_repeating_char(s):
        seen = {}
        for i, ch in enumerate(s):
            if ch in seen:
                return i
            seen[ch] = True
        return -1

    print(index_of_first_repeating_char("abcba"))   # Output: 3 (second 'b')
    print(index_of_first_repeating_char("abcdef"))  # Output: -1
    print(index_of_first_repeating_char("aabbcc"))  # Output: 1
    print(index_of_first_repeating_char(""))        # Output: -1


# Follow-up 3: your idea – use Counter to count first, then scan
def first_repeating_char_followup3():
    def first_repeating_char_with_counter(s):
        count = Counter(s)
        for ch in s:
            if count[ch] > 1:
                return ch
        return None

    print(first_repeating_char_with_counter("abcba"))     # Output: b
    print(first_repeating_char_with_counter("abcdef"))    # Output: None
    print(first_repeating_char_with_counter("aabbcc"))    # Output: a
    print(first_repeating_char_with_counter(""))          # Output: None
    print(first_repeating_char_with_counter("zxyxz"))     # Output: x


# Run all
if __name__ == "__main__":
    # print("Main Function:")
    # first_repeating_char_main()

    # print("\nFollow-up 1 (Case-insensitive):")
    # first_repeating_char_followup1()
    #
    # print("\nFollow-up 2 (Return Index):")
    # first_repeating_char_followup2()
    #
    print("\nFollow-up 3 (Using Counter - your idea):")
    first_repeating_char_followup3()
