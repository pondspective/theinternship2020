import math


def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False


def isFloatPrime(num):
    while True:
        num = 10*num
        if num == float("inf"):
            return False
        if (isPrime(math.floor(num))):
            return True
    return False


num = eval(input('Enter Float: '))
print(isFloatPrime(num))
