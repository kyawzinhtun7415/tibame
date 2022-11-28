# 2.     函數的練習-is_prime
#
# 寫一函數is_prime(n)用來判斷n是否為質數。
def is_prime(number):
    i = 2

    # divide the number and if it is not divisible, it is prime
    while i < number // 2 + 1:

        # if the number is divisble by i, it is not prime number
        if number % i == 0:
            return False
        i += 1
    return True

print(is_prime(3))