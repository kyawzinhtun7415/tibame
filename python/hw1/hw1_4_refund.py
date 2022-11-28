# 4.     選擇性敘述的練習-refund
#
# 輸入在某商店購物應付金額與實付金額。
# 實付金額小於應付金額，則印出”金額不足”。
# 實付金額等於應付金額，則印出”不必找錢”。
# 實付金額大於應付金額，則輸出找回金額最少的鈔票數和錢幣數。
# 假設幣值只有1000, 500, 100元紙鈔和50, 10, 5, 1元硬幣。
#
# 說明：若買了132元的商品，付1000元，應找回一張500元，三張100元，一個50元硬幣，一個10元硬幣，一個5元硬幣和三個1元硬幣。


# over 1200
def main():
    try:
        amount = int(input("應付金額"))
        pay = int(input("實付金額"))
    except ValueError:
        print("請輸入數字")
    else:
        print(customer_pay(amount, pay))


def customer_pay(amount, pay):
    if pay == amount:
        return "不必找錢"
    elif pay < amount:
        return "金額不足"
    elif pay > amount:
        return change(pay - amount)


def change(pay):
    five_hundred = 0
    one_hundred = 0
    fifty = 0
    ten = 0
    five = 0
    one = 0

    if pay > 500:
        five_hundred = pay // 500
        pay %= 500
    if pay > 100:
        one_hundred = pay // 100
        pay %= 100
    if pay > 50:
        fifty = pay // 50
        pay %= 50
    if pay > 10:
        ten = pay // 10
        pay %= 10
    if pay > 5:
        five = pay // 5
        pay %= 5

    one = pay
    return f"應找回{five_hundred}張500元，{one_hundred}張100元，{fifty}個50元硬幣，{ten}個10元硬幣，{five}個5元硬幣和{one}個1元硬幣。"


if __name__ == "__main__":
    main()
