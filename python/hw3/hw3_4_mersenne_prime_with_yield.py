# 4.     函數的練習-mersenne_prime
#
# 寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
#
# 提示：若質數滿足2^P-1=n (p為正整數)，則n為Mersenne Prime。
#
# 說明：當p=3時，2^3-1=7，故7為Mersenne Prime。
import time

def main():
    for i in get_mersenne_prime(5):
        print(i)

def get_mersenne_prime(index):
    i = 0
    number = 2
    while i < index:
        if is_mersenne_prime(number):
            # list.append(number)
            yield number
            i += 1
        number += 1


def is_mersenne_prime(number):
    p = 1
    while (2 ** p - 1) <= number:
        if 2 ** p - 1 == number:
            if is_prime(number):
                return True
        p += 1
    return False


def is_prime(number):
    i = 2

    # divide the number and if it is not divisible, it is prime
    while i < number // 2 + 1:

        # if the number is divisble by i, it is not prime number
        if number % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    main()
