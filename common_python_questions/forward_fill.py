def forward_fill_main():
    def forward_fill(lst):
        prev = None
        for i in range(len(lst)):
            if lst[i] is not None:
                prev = lst[i]
            elif prev is not None:
                lst[i] = prev
        return lst

    # Test
    data = [None, 2, None, None, 5, None, 7, None]
    print("Main:", forward_fill(data))


def forward_fill_followup1():
    def forward_fill_copy(lst):
        result = []
        prev = None
        for val in lst:
            if val is not None:
                prev = val
            result.append(prev if val is None else val)
        return result

    # Test
    data = [None, 2, None, None, 5, None, 7, None]
    print("Follow-up 1:", forward_fill_copy(data))


def forward_fill_followup2():
    def forward_fill_direction(lst, direction="forward"):
        result = lst[:]
        if direction == "forward":
            prev = None
            for i in range(len(result)):
                if result[i] is not None:
                    prev = result[i]
                elif prev is not None:
                    result[i] = prev
        elif direction == "backward":
            next_val = None
            for i in reversed(range(len(result))):
                if result[i] is not None:
                    next_val = result[i]
                elif next_val is not None:
                    result[i] = next_val
        return result

    # Test both directions
    data = [None, 2, None, None, 5, None, 7, None]
    print("Follow-up 2 - forward:", forward_fill_direction(data, "forward"))
    print("Follow-up 2 - backward:", forward_fill_direction(data, "backward"))


# 🔁 Advanced: Streaming generator version
def forward_fill_advanced():
    def streaming_forward_fill():
        prev = None
        while True:
            val = yield
            if val is not None:
                prev = val
                yield val
            else:
                yield prev

    # Test
    print("Advanced (Streaming):")
    stream = streaming_forward_fill()
    next(stream)  # Prime the generator
    for val in [None, 2, None, None, 5, None, 7, None]:
        print(stream.send(val))


if __name__ == "__main__":
    # forward_fill_main()
    # forward_fill_followup1()
    forward_fill_followup2()
    # forward_fill_advanced()
