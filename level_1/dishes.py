from typing import List


# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # Write your code here
    # start with the most naive way
    # go over all th elist, and compare each item with the past i  - k , if it is equal we  will not count it
    # then maybe we can use sliding window to make it more effecien
    #    if D[i] != D[max(0,i-K)]:

    count = 0
    last_k_eaten = []

    for i in range(len(D)):
        if D[i] not in last_k_eaten:
            count = count + 1
            last_k_eaten.append(D[i])
            if len(last_k_eaten) > K:
                last_k_eaten.pop(0)  # remove oldest eaten dish

    return count


from typing import List
# Write any import statements here
from collections import deque
def getMaximumEatenDishCount_2(N: int, D: List[int], K: int) -> int:
  # Write your code her
    last_k_eaten = deque()
    seen = set()
    count = 0

    for dish in D:
        if dish not in seen:
            count += 1
            last_k_eaten.append(dish)
            seen.add(dish)
            if len(last_k_eaten) > K:
                removed = last_k_eaten.popleft()
                seen.remove(removed)

    return count

def getMaximumEatenDishCount_3(N: int, D: List[int], K: int) -> int:
    last_k_eaten = []     # to track the order of last K eaten dishes
    seen = set()          # to check if dish is recently eaten in O(1)
    count = 0

    for dish in D:
        if dish not in seen:
            count += 1
            last_k_eaten.append(dish)
            seen.add(dish)

            if len(last_k_eaten) > K:
                # Remove the oldest dish from both list and set
                removed = last_k_eaten.pop(0)
                seen.remove(removed)

    return count
