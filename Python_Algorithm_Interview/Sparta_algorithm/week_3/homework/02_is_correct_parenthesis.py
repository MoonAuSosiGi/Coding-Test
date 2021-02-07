s = "(())()()"


def is_correct_parenthesis(string):

    check_stack = []
    for token in string:
        if token == ")":
            if check_stack[-1] == "(":
                check_stack.pop()
            else:
                return False
        else:
            check_stack.append(token)

    return len(check_stack) == 0


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!