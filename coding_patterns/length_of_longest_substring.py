def length_of_longest_substring(s):
    last_seen = {}  # char -> last index where it was seen
    left = 0  # start of the window
    best = 0  # max length found

    for right, ch in enumerate(s):
        # If we've seen this char inside the current window, move left
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1

        # Update the last seen index of this char
        last_seen[ch] = right

        # Update best length
        best = max(best, right - left + 1)

    return best
