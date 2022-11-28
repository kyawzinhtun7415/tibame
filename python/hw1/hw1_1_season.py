# 1.選擇性敘述的練習-season
#
# 輸入月份1~12月，判斷相對應的季節春、夏、秋、冬並印出。若不在此範圍則印出”輸入錯誤”。
# (備註︰春天是用 3、4和 5月，不是1、2和 3月)

def main():
    try:
        choice = int(input("輸入月份1~12月: "))
        print(seasons(choice))
    except ValueError:
        print("輸入錯誤")

def seasons(choice):
    if 1 <= choice <= 2 or choice == 12:
        return "春天"
    elif 3 <= choice <= 5:
        return "夏天"
    elif 6 <= choice <= 8:
        return "秋天"
    elif 9 <= choice <= 11:
        return "冬天"
    else:
        return "請輸入1到12月"

if __name__ == "__main__":
    main()