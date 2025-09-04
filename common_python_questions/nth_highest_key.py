def nth_highest_key_main(data=None, n=1):
    """
    Returns the key with the N-th highest value in the dictionary.
    If there are not enough unique values, return None.
    """
    if data is None:
        data = {'a': 10, 'b': 20, 'c': 30, 'd': 20}
    if n < 1:
        return None

    # Step 1: Get unique values and sort them descending
    unique_values = sorted(set(data.values()), reverse=True)
    if n > len(unique_values):
        return None

    nth_value = unique_values[n - 1]

    # Step 2: Return any key that has this value
    return [k for k, v in data.items() if v == nth_value]


# Follow-up 1: Return ALL keys with the N-th highest value, sorted alphabetically
def nth_highest_key_followup1(data=None, n=1):
    if data is None:
        data = {'a': 10, 'b': 20, 'c': 30, 'd': 20, 'e': 30}
    if n < 1:
        return []

    unique_values = sorted(set(data.values()), reverse=True)
    if n > len(unique_values):
        return []

    nth_value = unique_values[n - 1]
    return sorted([k for k, v in data.items() if v == nth_value])


# Follow-up 2: Use a heap to optimize for large datasets
import heapq

def nth_highest_key_followup2(data=None, n=1):
    if data is None:
        data = {'a': 10, 'b': 20, 'c': 30, 'd': 20, 'e': 5, 'f': 40}
    if n < 1:
        return []

    # Use a min-heap of size n
    min_heap = []
    seen = set()

    for val in data.values():
        if val not in seen:
            seen.add(val)
            heapq.heappush(min_heap, val)
            if len(min_heap) > n:
                heapq.heappop(min_heap)

    if len(min_heap) < n:
        return []

    nth_value = min_heap[0]
    return sorted([k for k, v in data.items() if v == nth_value])


# Test cases
if __name__ == "__main__":
    # print("Main Function:")
    # print(nth_highest_key_main({'a': 10, 'b': 20, 'c': 30, 'd': 20}, 2))  # ['b', 'd']
    # data = {'a': 10, 'b': 20, 'c': 30, 'd': 20}
    # print(data.get('a'))
    # print(data.fromkeys(['a', 'b', 'c', 'd']))

    #
    # print("\nFollow-up 1 (all keys sorted):")
    # print(nth_highest_key_followup1({'a': 10, 'b': 20, 'c': 30, 'd': 20, 'e': 30}, 1))  # ['c', 'e']
    #
    print("\nFollow-up 2 (optimized heap):")
    print(nth_highest_key_followup2({'a': 10, 'b': 20, 'c': 30, 'd': 20, 'e': 5, 'f': 40}, 3))  # ['b', 'd']
