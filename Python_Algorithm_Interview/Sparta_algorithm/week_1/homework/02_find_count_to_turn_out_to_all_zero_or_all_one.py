input =  "011110" # "01010" # "01001001101" # "0001100"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    checkDict = {}
    word = ""
    for i in range(len(string)):
        cur = string[i]
        next = string[(i + 1 < len(string)) and i+1 or i]
        word += cur

        if cur != next or i+1 == len(string):
            if cur in checkDict:
                checkDict[cur] += 1
            else:
                checkDict[cur] = 1
            word = ""

    return checkDict["0"] > checkDict["1"] and checkDict["1"] or checkDict["0"]

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)