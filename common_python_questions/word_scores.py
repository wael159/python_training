import heapq
import string

# Helper: letter score
def letter_score(c):
    """Returns the alphabetical score of a letter (a=1 to z=26)."""
    c = c.lower()
    if c in string.ascii_lowercase:
        return ord(c) - ord('a') + 1
    return 0

# Helper: word score
def word_score(word):
    """Computes the total score of a word by summing letter scores."""
    return sum(letter_score(c) for c in word)


# ----------------------------------------------
# Main Function
# ----------------------------------------------
def word_scores_main(words):
    """
    Returns words with their scores, sorted by descending score.
    Original order preserved if scores match.
    """
    scored = [(word, word_score(word)) for word in words]
    scored.sort(key=lambda x: -x[1])  # Sort by score descending
    return scored


# ----------------------------------------------
# Follow-up 1
# ----------------------------------------------
def word_scores_followup1(words):
    """
    Returns words with their scores, sorted by descending score.
    Tie-break alphabetically.
    """
    scored = [(word, word_score(word)) for word in words]
    scored.sort(key=lambda x: (-x[1], x[0]))  # Score descending, then alphabetically
    return scored


# ----------------------------------------------
# Follow-up 2 (using heap)
# ----------------------------------------------
def word_scores_followup2(words, k):
    """
    Returns the top K words with the highest scores.
    Uses heap for efficiency.
    """
    heap = []
    for word in words:
        score = word_score(word)
        heapq.heappush(heap, (-score, word))  # Max-heap via negative score

    result = []
    for _ in range(min(k, len(heap))):
        score, word = heapq.heappop(heap)
        result.append((word, -score))  # Convert score back to positive

    return result


# ----------------------------------------------
# Test Cases
# ----------------------------------------------
if __name__ == "__main__":
    words1 = ["abc", "cab", "bca", "zzz"]
    words2 = ["abc", "zzz", "aaa", "cab", "xyz"]
    words3 = ["Alpha", "beta", "Gamma!", "delta", "epsilon123"]

    print("🔹 Main Function:")
    print(word_scores_main(words1))
    # [('zzz', 78), ('abc', 6), ('cab', 6), ('bca', 6)]

    # print("\n🔹 Follow-up 1 (alphabetical tie-break):")
    # print(word_scores_followup1(words1))
    # # [('zzz', 78), ('abc', 6), ('bca', 6), ('cab', 6)]
    #
    # print("\n🔹 Follow-up 2 (Top 2 from words2):")
    # print(word_scores_followup2(words2, k=2))
    # # [('zzz', 78), ('xyz', 75)]
    #
    # print("\n🔹 Bonus test (with punctuation and case):")
    # print(word_scores_main(words3))
    # # Handles 'Gamma!' and 'epsilon123' properly (ignores non-letters)
