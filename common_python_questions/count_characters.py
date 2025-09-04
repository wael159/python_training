# ------------------------------------------------------------
# Meta Interview: count_characters
# ------------------------------------------------------------
# Main Question:
# Given a string, return a dictionary with counts of each character.
# ------------------------------------------------------------

# Main function implementation
def count_characters_main():
    def count_characters(s):
        result = {}
        for char in s:
            result[char] = result.get(char, 0) + 1
        return result

    # Test cases
    print("Test 1:", count_characters("banana"))     # {'b': 1, 'a': 3, 'n': 2}
    print("Test 2:", count_characters(""))           # {}
    print("Test 3:", count_characters("aaa"))        # {'a': 3}
    print("Test 4:", count_characters("Hello!"))     # {'H': 1, 'e': 1, 'l': 2, 'o': 1, '!': 1}


# ------------------------------------------------------------
# Follow-up 1:
# Only count alphabetic characters, case-insensitive.
# ------------------------------------------------------------
def count_characters_followup1():
    def count_alpha_lower(s):
        result = {}
        for char in s:
            if char.isalpha():
                char = char.lower()
                result[char] = result.get(char, 0) + 1
        return result

    # Test cases
    print("Test 1:", count_alpha_lower("Hello, World!"))   # {'h':1,'e':1,'l':3,'o':2,'w':1,'r':1,'d':1}
    print("Test 2:", count_alpha_lower("123 ABC abc"))     # {'a': 2, 'b': 2, 'c': 2}
    print("Test 3:", count_alpha_lower(""))                # {}
    print("Test 4:", count_alpha_lower("..."))             # {}


# ------------------------------------------------------------
# Follow-up 2:
# Use Counter for performance & readability.
# ------------------------------------------------------------
def count_characters_followup2():
    from collections import Counter

    def count_with_counter(s):
        return dict(Counter(c.lower() for c in s if c.isalpha()))

    # Test cases
    print("Test 1:", count_with_counter("Hello, World!"))  # {'h':1,'e':1,'l':3,'o':2,'w':1,'r':1,'d':1}
    print("Test 2:", count_with_counter("banana"))         # {'b':1,'a':3,'n':2}
    print("Test 3:", count_with_counter("123 ABC abc"))    # {'a':2,'b':2,'c':2}
    print("Test 4:", count_with_counter(""))               # {}


# ------------------------------------------------------------
# Advanced:
# Handle streaming input (data comes in chunks)
# ------------------------------------------------------------
class CharacterStreamCounter:
    def __init__(self):
        from collections import defaultdict
        self.counts = defaultdict(int)

    def process_chunk(self, chunk):
        for c in chunk:
            if c.isalpha():
                self.counts[c.lower()] += 1

    def get_counts(self):
        return dict(self.counts)


def test_stream_counter():
    counter = CharacterStreamCounter()
    counter.process_chunk("Hello, ")
    counter.process_chunk("World!!!")
    counter.process_chunk(" And More Letters...")
    print("Streaming result:", counter.get_counts())
    # Expected: {'h':1,'e':3,'l':5,'o':3,'w':1,'r':3,'d':1,'a':1,'n':1,'m':1,'t':2,'s':1}


# ------------------------------------------------------------
# Run All
# ------------------------------------------------------------
if __name__ == "__main__":
    print("=== Main Function ===")
    count_characters_main()

    print("\n=== Follow-up 1 (alpha only, case-insensitive) ===")
    count_characters_followup1()

    print("\n=== Follow-up 2 (optimized with Counter) ===")
    count_characters_followup2()

    print("\n=== Advanced (Streaming input) ===")
    test_stream_counter()
