# 輸入便利商店工讀生的工作時數，並計算其薪資。
# 60小時以內，時薪160元。
# 61~80小時，以時薪1.25倍計算。
# 81小時以上，以時薪1.5倍計算。
#
# 說明：薪資以累計方式計算。若工時為90小時，
# 則薪資為60*160 + 20*160*1.25 + 10*160*1.5元。


def main():
    try:
        total_hours = int(input("輸入便利商店工讀生的工作時數，並計算其薪資: "))
    except ValueError:
        print("請輸入時數")
    else:
        print("則薪資為", calculate(total_hours), "元")

def calculate(total_hours):
    wage = 160
    hours_left = 0
    salary = 0
    if total_hours >= 81:
        hours_over_81 = total_hours - 80
        salary = wage * hours_over_81 * 1.5
        hours_left = total_hours - hours_over_81
    if 61 <= hours_left <= 80:
        hours_under_81 = hours_left - 60
        salary += wage * hours_under_81 * 1.25
        hours_left -= hours_under_81
    if hours_left <= 60:
        salary += wage * hours_left
    return salary

if __name__ == "__main__":
    main()