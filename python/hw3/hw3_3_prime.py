# 3.     函數的練習-prime
#
# 寫一函數get_prime (n)用來找出第n個質數。

def is_prime(number):
    i = 2

    # divide the number and if it is not divisible, it is prime
    while i < number // 2 + 1:

        # if the number is divisble by i, it is not prime number
        if number % i == 0:
            return False
        i += 1
    return True


def prime(n):
    list = []
    i = 2
    index = 1
    # search prime numbers below this number
    while True:
        if is_prime(i):
            if index == n:
                return i
                break
            index += 1
        i += 1

print(prime(4))


