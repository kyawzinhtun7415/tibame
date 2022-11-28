# 2.迴圏的練習-perfect_number
#
# 一個數字若等於其所有因數的總和，則此數為perfect number。
# 找出100以內所有的完美數。
#
# 說明：6的因數為1, 2, 3，6=1+2+3，故6為完美數。
from functools import reduce


def main():
    print("100以內所有的完美數:", )
    print(*perfect_numbers(100), sep=", ")


def perfect_numbers(number):
    # search perfect number from 2 to 100
    list = []
    for i in range(2, 101):
        if divisors(i):
            list.append(i)
    return list


def divisors(number):
    divisors = []
    divisor = 1

    # get the divisors of the number into the list
    while divisor < number:
        if number % divisor == 0:
            divisors.append(divisor)
        divisor += 1

    # sum the divisors of the list
    sum_of_divisors = sum(divisors)

    # if the sum is equal to the number, then the number is the perfect number
    if number == sum_of_divisors:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
