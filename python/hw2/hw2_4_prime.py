# 4.迴圈的練習-prime
#
# 輸入一正整數，找出所有小於或等於的質數。

def main():
    number = get_int("輸入一正整數:")
    print("Prime numbers: ", end="")
    print(*prime(number), sep=", ")


def get_int(string):
    try:
        return int(input(string))
    except ValueError:
        print("請輸入一正整數")


def is_prime(number):
    i = 2

    # divide the number and if it is not divisible, it is prime
    while i < number // 2 + 1:

        # if the number is divisble by i, it is not prime number
        if number % i == 0:
            return False
        i += 1
    return True


def prime(number):
    list = []
    i = 2
    # search prime numbers below this number
    while i < number:
        if is_prime(i):
            list.append(i)
        i += 1
    return list


if __name__ == "__main__":
    main()
