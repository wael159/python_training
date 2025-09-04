def fill_in_the_blanks(input_lst):
    last_seen = None
    result = []

    for value in input_lst:
        if value is not None:  # non-null value
            last_seen = value
            result.append(value)
        else:  # null value
            if last_seen is not None:
                result.append(last_seen)
            else:
                result.append(None)  # still None if nothing before it

    return result


# Test cases
print(fill_in_the_blanks([1, None, 2, 3, None, None, 5, None]))  # [1, 1, 2, 3, 3, 3, 5, 5]
print(fill_in_the_blanks([None, 8, None]))  # [None, 8, 8]
print(fill_in_the_blanks([1, None, 2]))  # [1, 1, 2]
print(fill_in_the_blanks([5, None, 5, None]))  # [5, 5, 5, 5]
