from typing import List

# ------------------------------------------------------------
# 1. getSum
# ------------------------------------------------------------
# Given 3 integers A, B, and C:
# Return their sum only if all are less than or equal to 100.
# Otherwise, return 0.

def getSum(A: int, B: int, C: int) -> int:
    if A > 100 or B > 100 or C > 100:
        return 0
    return sum([A, B, C])


# ------------------------------------------------------------
# 2. getWrongAnswers
# ------------------------------------------------------------
# Given a string C consisting of characters 'A' and 'B',
# return a new string where each 'A' is replaced with 'B',
# and each 'B' is replaced with 'A'.

def getWrongAnswers(N: int, C: str) -> str:
    flip = {'A': 'B', 'B': 'A'}
    return ''.join(flip[ch] for ch in C)


# ------------------------------------------------------------
# 3. getHitProbability
# ------------------------------------------------------------
# Given a 2D grid G of R rows and C columns with 0s and 1s:
# Return the probability of a hit (value 1) in the grid.

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    total_hits = sum(map(sum, G))
    total_cells = R * C
    return total_hits / total_cells if total_cells != 0 else 0.0


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
if __name__ == "__main__":
    print("getSum Tests:")
    print(getSum(10, 20, 30))    # Expected: 60
    print(getSum(100, 100, 100)) # Expected: 300
    print(getSum(101, 20, 30))   # Expected: 0
    print()

    print("getWrongAnswers Tests:")
    print(getWrongAnswers(4, "ABBA"))  # Expected: "BAAB"
    print(getWrongAnswers(5, "AAAAA")) # Expected: "BBBBB"
    print(getWrongAnswers(3, "BAB"))   # Expected: "ABA"
    print()

    print("getHitProbability Tests:")
    G1 = [
        [0, 1, 0],
        [1, 0, 1]
    ]
    print(getHitProbability(2, 3, G1))  # Expected: 0.5

    G2 = [
        [1, 1],
        [1, 1]
    ]
    print(getHitProbability(2, 2, G2))  # Expected: 1.0

    G3 = [
        [0, 0],
        [0, 0]
    ]
    print(getHitProbability(2, 2, G3))  # Expected: 0.0
