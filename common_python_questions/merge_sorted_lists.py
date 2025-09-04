import heapq

# ---------------- Main Function ----------------
def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merged = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


# ---------------- Follow-up 1: Remove Duplicates ----------------
def merge_no_duplicates(l1, l2):
    i, j = 0, 0
    merged = []
    prev = None
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            val = l1[i]
            i += 1
        elif l1[i] > l2[j]:
            val = l2[j]
            j += 1
        else:
            val = l1[i]
            i += 1
            j += 1
        if val != prev:
            merged.append(val)
            prev = val

    while i < len(l1):
        if l1[i] != prev:
            merged.append(l1[i])
            prev = l1[i]
        i += 1

    while j < len(l2):
        if l2[j] != prev:
            merged.append(l2[j])
            prev = l2[j]
        j += 1

    return merged


# ---------------- Follow-up 2: Merge K Sorted Lists ----------------
def merge_k_lists(lists):
    min_heap = []
    result = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))

    return result


# ---------------- Advanced: Streaming Merge for Large Data ----------------
def merge_streams(g1, g2):
    a = next(g1, None)
    b = next(g2, None)
    while a is not None and b is not None:
        if a <= b:
            yield a
            a = next(g1, None)
        else:
            yield b
            b = next(g2, None)
    while a is not None:
        yield a
        a = next(g1, None)
    while b is not None:
        yield b
        b = next(g2, None)


# ---------------- Tests ----------------
if __name__ == "__main__":
    # print("=== Main Question ===")
    # print("Input: [1, 3, 5, 7], [2, 4, 6, 8]")
    # print("Output:", merge_sorted_lists([1, 3, 5, 7], [2, 4, 6, 8]))
    # print()

    # print("=== Follow-up 1: Remove Duplicates ===")
    # print("Input: [1, 3, 5, 5, 7], [2, 3, 4, 6, 7, 8]")
    # print("Output:", merge_no_duplicates([1, 3, 5, 5, 7], [2, 3, 4, 6, 7, 8]))
    # print()

    # print("=== Follow-up 2: Merge K Sorted Lists ===")
    # k_lists = [
    #     [1, 4, 5],
    #     [1, 3, 4],
    #     [2, 6]
    # ]
    # print("Input:", k_lists)
    # print("Output:", merge_k_lists(k_lists))
    # print()
    #
    print("=== Advanced: Streaming Merge ===")
    g1 = iter([1, 4, 7, 10])
    g2 = iter([2, 5, 6, 11])
    print("Input: stream1=[1,4,7,10], stream2=[2,5,6,11]")
    print("Output:", list(merge_streams(g1, g2)))
