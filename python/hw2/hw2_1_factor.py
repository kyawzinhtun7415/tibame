# 1. 迴圏的練習-factor
#
# 輸入一正整數，求其所有的因數。
# 說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36,

def main():
    number = get_int("輸入一正整數，求其所有的因數 ")
    print(*factor(number), sep=", ")

def get_int(string):
    try:
        return int(input(string))
    except ValueError:
        print("請輸入數字")

def factor(number):
    list = []
    factor = 1
    while factor <= number:
        if number % factor == 0:
            list.append(factor)
        factor += 1
    return list

if __name__ == "__main__":
    main()