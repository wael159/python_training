def character_frequency(s, c):
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count


# Examples
print(character_frequency("Mississippi", "s"))  # 4
print(character_frequency("Rainbow", "j"))      # 0
print(character_frequency("Mirror", "r"))       # 3
