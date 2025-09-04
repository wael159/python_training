
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    count = 0
    for i in range(N):
        if C[i] == 'A':
            # Check for 'P' before A and 'B' after A
            for j in range(max(0, i - Y), i - X + 1):
                if C[j] == 'P':
                    for k in range(i + X, min(N, i + Y + 1)):
                        if C[k] == 'B':
                            count += 1

            # Check for 'B' before A and 'P' after A
            for j in range(max(0, i - Y), i - X + 1):
                if C[j] == 'B':
                    for k in range(i + X, min(N, i + Y + 1)):
                        if C[k] == 'P':
                            count += 1
    return count


from typing import List

def getArtisticPhotographCount_2(N: int, C: str, X: int, Y: int) -> int:
    # Precompute prefix sums for 'P' and 'B'
    photos_before = [0] * (N + 1)
    bgs_before = [0] * (N + 1)
    actors = []

    for i, ch in enumerate(C):
        photos_before[i + 1] = photos_before[i] + (1 if ch == 'P' else 0)
        bgs_before[i + 1] = bgs_before[i] + (1 if ch == 'B' else 0)
        if ch == 'A':
            actors.append(i)

    total = 0
    for a in actors:
        # Define left and right valid ranges
        left_start = max(0, a - Y)
        left_end = max(0, a - X + 1)
        right_start = min(N, a + X)
        right_end = min(N, a + Y + 1)

        # Count photographers and backdrops using prefix sums
        left_photographers = photos_before[left_end] - photos_before[left_start]
        right_backdrops = bgs_before[right_end] - bgs_before[right_start]
        total += left_photographers * right_backdrops

        left_backdrops = bgs_before[left_end] - bgs_before[left_start]
        right_photographers = photos_before[right_end] - photos_before[right_start]
        total += left_backdrops * right_photographers

    return total


# ✅ Test it here
if __name__ == "__main__":
    # Example 1
    N = 5
    C = "APABA"
    X = 1
    Y = 2
    print("Test 1 Output:", getArtisticPhotographCount_2(N, C, X, Y))  # Expected: 1

    # Example 2 - More complex
    N = 7
    C = "PABAPBP"
    X = 1
    Y = 3
    print("Test 2 Output:", getArtisticPhotographCount_2(N, C, X, Y))  # You can debug this

    # Edge case - No 'A's
    N = 4
    C = "PPBB"
    X = 1
    Y = 2
    print("Test 3 Output:", getArtisticPhotographCount_2(N, C, X, Y))  # Expected: 0

    # Edge case - All 'A's
    N = 3
    C = "AAA"
    X = 1
    Y = 1
    print("Test 4 Output:", getArtisticPhotographCount_2(N, C, X, Y))  # Expected: 0

