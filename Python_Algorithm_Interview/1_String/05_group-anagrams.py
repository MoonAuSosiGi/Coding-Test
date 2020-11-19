import collections
def groupAnagrams(strs : [str]):
    resultDic = collections.defaultdict(list)

    for word in strs:
        resultDic[''.join(sorted(list(word)))].append(word)
        # 아래에 해당하는 루틴을 한줄로 표현 가능 (위와 같이)
        # words = list(word)
        # words.sort()
        # key = "".join(words)
        # resultDic[key].append(word)

    print(list(resultDic.values()))

groupAnagrams(["eat","tea","tan","ate","nat","bat"])