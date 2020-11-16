
def reorderLogFiles(logs: [str]):
    digits, letters = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # 식별자를 제외한 첫번재 요소를 키로 잡고, 동일할 경우 식별자를 기준으로 정렬
    letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))

    return letters + digits


print(reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))