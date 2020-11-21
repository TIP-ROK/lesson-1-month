# 9! => 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

def factorial(n, result=1):
    if n == 1:
        return result
    result = result * n
    print(result)
    return factorial(n - 1, result)


print(factorial(9))