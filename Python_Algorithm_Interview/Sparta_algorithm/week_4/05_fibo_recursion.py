input = 100


def fibo_recursion(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765