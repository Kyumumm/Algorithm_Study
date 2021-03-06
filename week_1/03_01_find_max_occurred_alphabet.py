input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        index = ord(char) - ord("a")
        alphabet_occurrence_array[index] += 1

    max_occ = 0
    max_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occ:
            max_occ = alphabet_occurrence
            max_index = index

    return chr(max_index + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)
