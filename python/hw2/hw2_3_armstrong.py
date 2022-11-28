# 3.迴圏的練習-amstrong
#
# Amstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。
# 找出所有的Amstrong數。
#
# 說明：153=1^3+5^3+3^3，故153為Amstrong數。
#  (2^3 表示 2 的 3 次方, 3^3 表示 3 的 3 次方)

def main():
    print(*armstrong(), sep=", ")


def armstrong():
    list = []
    for i in range(100, 1000):
        if is_armstrong(str(i)):
            list.append(i)
    return list


def is_armstrong(number):
    armstrong = 0

    # iterate over the number and exponent each individual number
    for i in number:
        armstrong += int(i) ** 3

    if armstrong == int(number):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
