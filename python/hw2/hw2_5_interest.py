# 5.迴圈敘述的練習-interest
#
# 某人A以10%單利投資100000元，某人B則以5%複利投資100000元。計算多少年後某人B的投資可以超過某人A，並將此時兩人錢數印出。(27年後)
#
# 提示：單利公式：P(1+r*n)    複利公式：P(1+r)^n
# P：本金，r：利率，n：多少年
#
# (備註︰(1+r)^n 表示 (1+r) 的 n 次方)

def main():
    single_rate = 0.1
    compound_rate = 0.05
    year = 1
    deposit = 100000
    while True:
        a_deposit = single_interest(deposit, year, single_rate)
        b_deposit = compound_interest(deposit, year, compound_rate)
        if b_deposit > a_deposit:
            print("A錢數", str(a_deposit))
            print("B錢數", str(b_deposit))
            print(f"B投資在{year}年後超過A投資")
            break
        year += 1


def single_interest(deposit, year, interest):
    return deposit * (1 + interest * year)


def compound_interest(deposit, year, interest):
    return deposit * (1 + interest) ** year


if __name__ == "__main__":
    main()
