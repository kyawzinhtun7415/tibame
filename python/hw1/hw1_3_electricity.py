# 輸入何種用電和度數，計算出需繳之電費。
# 電力公司使用累計方式來計算電費，分工業用電及家庭用電。
#
#                                    家庭用電        工業用電
#
#    120度(含)以下         1.63元               0.5元
#
#    121~330(含)度        2.38元               0.5元
#
#    330度以上               3.52元               0.5元


def main():
    try:
        type = int(input("輸入何種用電，計算出需繳之電費\n1.家庭用電\n2.工業用電\n請輸入1或2\n"))
        unit = int(input("輸入何種度數，計算出需繳之電費: "))
    except ValueError:
        print("請只輸入何種用電和度數")
    else:
        print(home_or_industry(type, unit), "元")

def home_or_industry(type, unit):
    if type == 1:
        return home(unit)
    elif type == 2:
        return industry(unit)
    else:
        return ("請輸入1或2")

def home(unit):
    rate_330 = 3.52
    rate_120 = 2.38
    normal_rate = 1.63
    if unit >= 330:
        return ((unit - 330) * rate_330) + (110 * rate_120) + (120 * normal_rate)
    elif 121 <= unit < 330:
        return ((unit - 120) * rate_120) + (120 * normal_rate)
    elif unit <= 120:
        return unit * normal_rate
    else:
        return "請輸入數字"

def industry(unit):
    rate = 0.5
    return unit * 0.5

if __name__ == "__main__":
    main()