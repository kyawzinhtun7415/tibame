# 5.     迴圏的練習-password
#
# 出現”請輸入密碼”的提示，使用者有最多三次輸入的機會。
# 若輸入正確，則印出”密碼輸入正確，歡迎使用本系統！”。
# 若輸入不正確，再次出現”請輸入密碼”的提示。
# 若三次輸入不正確，則印出”密碼輸入超過三次！”，並結束程式的執行。
import sys
def main():
    real_password = "123"
    turn = 3
    while turn > 0:
        input_password = input("請輸入密碼 ")
        if input_password != real_password:
            print("不正確，再次出現請輸入密碼 ")
        else:
            sys.exit("密碼輸入正確，歡迎使用本系統！")
        turn -= 1
    sys.exit("密碼輸入超過三次！")

if __name__ == "__main__":
    main()