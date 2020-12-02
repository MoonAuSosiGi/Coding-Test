
# 홀수, 짝수 체크
# bbaabbd
# 홀수 0 1
def expandCheck(left : int, right : int, s : str) -> [str]:
    while left >= 0 and right <= len(s) and s[left] == s[right-1]:
        left -= 1
        right += 1
    return s[left+1 : right-1]

def longestPalindrome(s : str):
    # "babad" -> "bab
    # bababd -> babab 홀수
    # babba -> abba 짝수

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s)):
        result = max(result,
                     expandCheck(i, i+1, s),
                     expandCheck(i, i+2, s),
                     key=len)

    return result
print( longestPalindrome("1234543212232") )