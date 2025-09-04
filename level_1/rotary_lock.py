from typing import List


# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    # first it a cyclic array
    # we need to compatre bothways and choose the min one
    # this is mean that for example when starting with 1 and we want to move to  9 then we have two way from 1 to 9 which 9 sec, or from 1 to 9 backward which is 2 second
    # it can be C[N-0]-N[0] which is C[N-i]-N[i]
    # the naive ways is to go over the list one by one, and check the differnece in both way and take the min
    list_num = range(1, N + 1)
    sum = 0
    i = 0

    # first we need to check the first element, from where we can start, so if it was not 1, then we should check the min way on how to get the min path
    # then we will check the differences between the current item vs the prev item, for example if 4 - 9 < 0 then we need also to check on the other way , but if it was positive then we can continu
    # we need to check the first element:
    if C[0] != 1:
        num_idx_1 = list_num.index(1)
        num_idx_2 = list_num.index(C[0])
        min_diff = min(((num_idx_1 - num_idx_2) % N), ((num_idx_2 - num_idx_1) % N))
        sum = sum + min_diff
    for num in C:
        # lets say that we can find the min way - for each item in C list we check in both way of the cycle, what is the min path for it
        if i < len(C) - 1:
            num_idx_1 = list_num.index(num)
            num_idx_2 = list_num.index(C[i + 1])
            min_diff = min(((num_idx_1 - num_idx_2) % N), ((num_idx_2 - num_idx_1) % N))
            # then we do sum based on diff_1
            sum = sum + min_diff
        i = i + 1

    return sum


from typing import List

def getMinCodeEntryTime_2(N: int, M: int, C: List[int]) -> int:
    total_time = 0
    current = 1  # Start from position 1

    for target in C:
        # Compute clockwise and counter-clockwise distances
        clockwise = (target - current) % N
        counter_clockwise = (current - target) % N
        total_time += min(clockwise, counter_clockwise)
        current = target  # Move to the new position

    return total_time

