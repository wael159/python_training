from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S.sort()
    count = 0

    # Start of the seat range
    prev_end = 0

    for s in S:
        # The first seat that must remain empty before this diner
        left = s - K

        # The last free seat before that zone starts
        start = prev_end + 1
        end = left - 1

        if start <= end:
            count += (end - start + 1) // (K + 1)

        # Update prev_end to the last blocked seat by this diner
        prev_end = s + K

    # Handle the space after the last occupied seat
    if prev_end < N:
        start = prev_end + 1
        end = N
        count += (end - start + 1) // (K + 1)

    return count


def getMaxAdditionalDinersCount_2(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
    seats = [0] * N  # 0 = available, 1 = blocked or occupied

    # Step 1: Mark existing diners and block their neighbors
    for s in S:
        for i in range(max(0, s - K - 1), min(N, s + K)):
            seats[i] = 1

    # Step 2: Greedily place new diners
    count = 0
    i = 0
    while i < N:
        if seats[i] == 0:
            count += 1
            # Block this seat and its K neighbors
            for j in range(max(0, i - K), min(N, i + K + 1)):
                seats[j] = 1
            i += K + 1  # skip blocked area
        else:
            i += 1

    return count


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    accepted_diff = Y - X + 1
    temp_list = []
    count = 0
    # cnvert thr str to list"
    list_chars = list(C)
    str_length = len(C)

    # we wil search about the A apeerance, and check values of P an A which is in range of accepted_diff, so if we have it then
    # we count it

    for i in range(len(list_chars)):
        if list_chars[i] == 'A' and i != 0:
            # we search about P and B if it is found in the ranges in the righr or in the left:
            for j in range(Y):
                left = i - j - 1
                first_right = i + X
                second_right = i + Y + 1
                if list_chars[max(left, 0)] == 'P' and 'B' in list_chars[first_right:min(second_right, str_length)]:
                    count = count + 1
                elif list_chars[max(left, 0)] == 'B' and 'P' in list_chars[first_right:min(second_right, str_length)]:
                    count = count + 1

    return count




def getMaxAdditionalDinersCount_3(N: int, K: int, M: int, S: List[int]) -> int:
    # If no seats are occupied, fill the entire row using the spacing formula.
    if M == 0:
        return (N + K) // (K + 1)

    occupied = sorted(s - 1 for s in S)  # convert to 0-indexed and sort
    total = 0

    # Segment 1: seats before the first occupied seat
    usable_before_first = occupied[0] - K  # positions 0 .. occupied[0] - K - 1
    if usable_before_first > 0:
        total += (usable_before_first + K) // (K + 1)

    # Segment 2: gaps between consecutive occupied seats
    for i in range(M - 1):
        start_pos = occupied[i] + K + 1  # first available after current diner
        end_pos = occupied[i + 1] - K - 1  # last available before next diner
        usable_len = end_pos - start_pos + 1
        if usable_len > 0:
            total += (usable_len + K) // (K + 1)

    # Segment 3: seats after the last occupied seat
    first_after_last = occupied[-1] + K + 1
    usable_after_last = N - first_after_last
    if usable_after_last > 0:
        total += (usable_after_last + K) // (K + 1)

    return total


if __name__ == "__main__":
    # print("Test 1: ", getMaxAdditionalDinersCount_3(10, 1, 2, [2, 6]))  # Expected: 3
    # print("Test 2: ", getMaxAdditionalDinersCount_3(15, 2, 3, [11, 6, 14]))      # Expected: 1
    # print("Test 3: ", getMaxAdditionalDinersCount(5, 2, 1, [3]))      # Expected: 0
    # print("Test 4: ", getMaxAdditionalDinersCount(15, 2, 2, [5, 11])) # Expected: 2
    # print("Test 5: ", getMaxAdditionalDinersCount(100, 1, 0, []))     # Expected: 50
    # print("Test 6: ", getMaxAdditionalDinersCount(10, 2, 1, [1]))     # Expected: 2
    print("Test 7: ", getMaxAdditionalDinersCount_3(20, 2, 3, [4, 10, 18]))  # Expected: 3
