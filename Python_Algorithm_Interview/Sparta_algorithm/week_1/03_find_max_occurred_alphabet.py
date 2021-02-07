input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    string = string.lower()
    for token in string:
        if token.isalpha():
            alphabet_occurrence_array[ord(token) - ord('a')] += 1

    max_num = alphabet_occurrence_array[0]
    index = 0
    for i in range(len(alphabet_occurrence_array)):
        num = alphabet_occurrence_array[i]
        if num > max_num:
            max_num = num
            index = 0

    return chr(index + ord('a'))


result = find_max_occurred_alphabet(input)
print(result)