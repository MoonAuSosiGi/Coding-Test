from collections import deque

balanced_parentheses_string = ")(" #"(()())()" #"()))((()"


# 균형잡힌 괄호 문자열 -> 올바른 괄호 문자열
# 올바른 괄호 문자열?

def is_correct_parenthesis(string): # 올바른 괄호 문자열인지
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0

def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u,v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    v = ''.join(list(queue))
    return u,v

def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string


# 입력이 빈 문자열인 경우, 빈문자열 반환
def change_to_correct_parenthesis(string):
    if string == "":
        return ""
    # 2. 문자열 w 를 두 균형잡힌 괄호 문자열 u v 로 분리
    # 단 u는 균형잡힌 문자열로 더 이상 분리가 불가능해야함.
    # v는 빈 문자열이 될 수 있다.
    # ( ) 갯수가 같아야 함 -> 균형잡힌 괄호 문자열
    u, v = separate_to_u_v(string)

    # 3. 문자열 u가 올바른 괄호 문자열이라면, 문자열 v에 대해 1단계부터 수행
    # 3-1 수행한 결과 문자열을 u에 이어 붙인뒤 반환
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)
    # 4. u가 올바른 괄호 문자열이 아니라면.
    # 4-1 빈 문자열에 첫번째 문자로 (를 붙임
    # 4-2 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙임
    # 4-3 )를 다시 붙임
    # 4-4. u의 첫번째 문자와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    return change_to_correct_parenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!


# '(' 와 ')' 로만 이루어진 문자열이 있을 경우, '(' 의 개수와 ')' 의 개수가 같다면 이를 균형잡힌 괄호 문자열이라고 부릅니다.
# 그리고 여기에 '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부릅니다.
# 예를 들어, "(()))("와 같은 문자열은 균형잡힌 괄호 문자열 이지만 올바른 괄호 문자열은 아닙니다.
# 반면에 "(())()"와 같은 문자열은 균형잡힌 괄호 문자열 이면서 동시에 올바른 괄호 문자열 입니다.
#
# '(' 와 ')' 로만 이루어진 문자열 w가 균형잡힌 괄호 문자열 이라면 다음과 같은 과정을 통해 올바른 괄호 문자열로 변환할 수 있습니다.
#
# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
# 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
# 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
# 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
# 4-3. ')'를 다시 붙입니다.
# 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
# 4-5. 생성된 문자열을 반환합니다.
#
# 균형잡힌 괄호 문자열 p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 올바른 괄호 문자열로 변환한 결과를 반환하시오.