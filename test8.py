def Main(num):
    result = get_fibonacci(num)  
    return result


def get_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    n1 = n - 1
    n2 = n - 2
    fibr1 = get_fibonacci(n1)
    fibr2 = get_fibonacci(n2)
    res = fibr1 + fibr2
    return res
