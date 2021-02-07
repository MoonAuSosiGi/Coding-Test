input = 20


def find_prime_list_under_number(number):
    primeList = []
    for i in range(2,number + 1):

        for j in primeList:
            print(str(j))
            if i % j == 0 and j * j <= i:
                break
        else:
            primeList.append(i)
    return primeList


result = find_prime_list_under_number(input)
print(result)