all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

#del 을 통해 dict의 요소를 제거할 수 있음
def get_absent_student(all_array, present_array):
    dict = {}
    result = []
    for name in present_array:
        dict[name] = name

    for name in all_array:
        if (name in dict) is False:
            result.append(name)
    return result


print(get_absent_student(all_students, present_students))