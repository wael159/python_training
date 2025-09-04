from typing import List


# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    # first of all we can take the min value from the list, and based kn tnaht we will decide if we can defate it or ot
    # so then we can ditract each element by the min value, and check if there iz zero int he list then we cannot defalte it
    # we need to check also the max, if the max is the first one
    # we the list was sorted in a revers way then we return -1
    # for the first case we need to mark the value which is not ok for example 5 and 6 are not ok
    # so what we can do is we take the indexes of this values, and check the difference with the prev vs the one after , if the dif > 1 , then we should change two elements
    count = 0
    for i in range(N - 2, -1, -1):  # start from second-last down to first
        if R[i] >= R[i + 1]:
            new_val = R[i + 1] - 1
            if new_val < 1:
                return -1  # impossible to deflate below 1
            R[i] = new_val
            count += 1
    return count

