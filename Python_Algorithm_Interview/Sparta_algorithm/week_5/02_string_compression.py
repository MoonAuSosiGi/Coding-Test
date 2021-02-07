input = "abcabcabcabcdededededede"
#"abc abc abc abc ded ede ded ede"

def string_compression(string):
    min_count = 0
    for token_count in range(1, len(string) // 2 + 1):
        count = 1
        result = ""
        prev = ""
        for i in range(0,len(string), token_count):
            word = string[i:i+token_count]
            if prev != "" and prev != word:
                if count > 1:
                    result += str(count) + prev
                else:
                    result += prev
                count = 1
            if prev == word:
                count += 1
            prev = word

            if i + token_count >= len(string):
                if count > 1:
                    result += str(count) + prev
                else:
                    result += prev
        if min_count == 0:
            min_count = len(result)
        elif min_count > len(result):
            min_count = len(result)
    return min_count


print(string_compression(input))  # 14 가 출력되어야 합니다!

# 아래는 다른사람 코드
# input = "abcabcabcabcdededededede"
#
#
# def string_compression(string):
#     n = len(string)
#     compression_length_array = []  # 1~len까지 압축했을때 길이 값
#
#     for split_size in range(1, n // 2):
#         compressed = ""
#         # string 갯수 단위로 쪼개기 *
#         splited = [
#             string[i:i + split_size] for i in range(0, n, split_size)
#         ]
#         count = 1
#
#         for j in range(1, len(splited)):
#             prev, cur = splited[j - 1], splited[j]
#             if prev == cur:
#                 count += 1
#             else:  # 이전 문자와 다르다면
#                 if count > 1:
#                     compressed += (str(count) + prev)
#                 else:  # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
#                     compressed += prev
#                 count = 1  # 초기화
#         if count > 1:
#             compressed += (str(count) + splited[-1])
#         else:  # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
#             compressed += splited[-1]
#         compression_length_array.append(len(compressed))
#
#     return min(compression_length_array)  # 최솟값 리턴
#
#
# print(string_compression(input))  # 14 가 출력되어야 합니다!