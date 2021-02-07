def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    string = string.lower()
    for token in string:
        if token.isalpha():
            alphabet_occurrence_array[ord(token) - ord('a')] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))