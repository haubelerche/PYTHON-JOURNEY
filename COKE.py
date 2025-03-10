mustpay = 50
while mustpay > 0:
    print("Amount Due:", mustpay)

    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        mustpay -= coin
change= abs(mustpay)
print("Change Owed:", change)
