input = "abadabac "


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        index = ord(char) - ord("a")
        alphabet_occurrence_array[index] += 1

    alphabet_occurrence = []
    for temp in range(len(alphabet_occurrence_array)):
        array_list = alphabet_occurrence_array[temp]
        if array_list == 1:
            alphabet_occurrence.append(chr(temp + ord("a")))

    for char in string:
        if char in alphabet_occurrence:
            return char

    return "-"


result = find_not_repeating_character(input)
print(result)
