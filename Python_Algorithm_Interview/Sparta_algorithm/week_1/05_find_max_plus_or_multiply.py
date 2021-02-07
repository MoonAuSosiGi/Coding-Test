input =[1,1,1,1,2] #[0, 3, 5, 6, 1, 2, 4]

# 0 과 1일때 곱하는 것보다 더하는게 이득
def find_max_plus_or_multiply(array):
    multiply_sum = 0

    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number

    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)