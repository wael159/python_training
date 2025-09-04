from typing import List


# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    # Write your code here
    # first of all we can take the max value from the list
    # then we can check all the permuatation of 1 and 2 which can give us the sum of this max number
    # so then we will go with the values that we got for this, for examle for 6 we have 2,2,2 or 2,1,1,2 or 2,1,1,1,1
    # so we start with the min set and check if we can get the sum which is in the list from this numebrs that we have
    # another approach is to check if th numbers are or not eve, and based on that we can also take the correct set which inclde 1 and 2
    # or we can do somthing else, whcih first we can take all the min permutation and check the possible sum from this permutation if it in in the list or not

    contains_odd = any(score % 2 == 1 for score in S)

    # The largest score determines how many 2-point problems are needed.
    highest_score = max(S)

    # Minimal problem count = number of 2-point problems + possibly one 1-point problem.
    return (highest_score // 2) + (1 if contains_odd else 0)


