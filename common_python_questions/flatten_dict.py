def flatten_dict_main():
    """
    Flatten a nested dictionary using dot as a separator.
    Example:
    Input: {'a': {'b': {'c': 1}}, 'd': 2}
    Output: {'a.b.c': 1, 'd': 2}
    """
    def flatten(d, parent_key="", sep="."):
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(flatten(v, new_key, sep=sep))
            else:
                items[new_key] = v
        return items

    test_input = {
        "a": {
            "b": {
                "c": 1
            }
        },
        "d": 2
    }

    expected_output = {
        "a.b.c": 1,
        "d": 2
    }

    result = flatten(test_input)
    print("Input:", test_input)
    print("Flattened:", result)
    print("Expected:", expected_output)
    assert result == expected_output
    print("✅ Passed Main Test")


def flatten_dict_followup1():
    """
    Flatten a nested dictionary using custom separator.
    Example:
    Input: {'x': {'y': {'z': 99}}, 'm': 3} with sep='-'
    Output: {'x-y-z': 99, 'm': 3}
    """
    def flatten(d, parent_key="", sep="-"):
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(flatten(v, new_key, sep=sep))
            else:
                items[new_key] = v
        return items

    test_input = {
        "x": {
            "y": {
                "z": 99
            }
        },
        "m": 3
    }

    expected_output = {
        "x-y-z": 99,
        "m": 3
    }

    result = flatten(test_input, sep="-")
    print("Input:", test_input)
    print("Flattened:", result)
    print("Expected:", expected_output)
    assert result == expected_output
    print("✅ Passed Follow-up 1 Test")


def flatten_dict_followup2():
    """
    Flatten a nested dictionary that includes lists.
    Example:
    Input: {'a': {'b': [1, {'c': 2}]}}
    Output: {'a.b.0': 1, 'a.b.1.c': 2}
    """
    def flatten(d, parent_key="", sep="."):
        items = {}
        if isinstance(d, dict):
            for k, v in d.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
                items.update(flatten(v, new_key, sep=sep))
        elif isinstance(d, list):
            for i, v in enumerate(d):
                new_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
                items.update(flatten(v, new_key, sep=sep))
        else:
            items[parent_key] = d
        return items

    test_input = {
        "a": {
            "b": [1, {"c": 2}]
        }
    }

    expected_output = {
        "a.b.0": 1,
        "a.b.1.c": 2
    }

    result = flatten(test_input)
    print("Input:", test_input)
    print("Flattened:", result)
    print("Expected:", expected_output)
    assert result == expected_output
    print("✅ Passed Follow-up 2 Test")


# Optional: Generator-based flattening for large streaming dicts
def flatten_generator_example():
    def flatten_generator(d, parent_key="", sep="."):
        if isinstance(d, dict):
            for k, v in d.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
                yield from flatten_generator(v, new_key, sep=sep)
        elif isinstance(d, list):
            for i, v in enumerate(d):
                new_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
                yield from flatten_generator(v, new_key, sep=sep)
        else:
            yield (parent_key, d)

    test_input = {
        "root": {
            "data": [1, 2, {"deep": {"leaf": 42}}]
        }
    }

    print("Streaming Flattened Key-Value Pairs:")
    for k, v in flatten_generator(test_input):
        print(f"{k}: {v}")


# Run all test cases
if __name__ == "__main__":
    # print("=== Main Function ===")
    # flatten_dict_main()

    # print("\n=== Follow-up 1: Custom Separator ===")
    # flatten_dict_followup1()
    #
    print("\n=== Follow-up 2: Handle Lists ===")
    flatten_dict_followup2()
    #
    # print("\n=== Advanced: Generator Example ===")
    # flatten_generator_example()
