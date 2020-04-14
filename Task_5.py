# Task 5

profit = int(input("Enter a profit: "))
cost = int(input("Enter a cost: "))

if profit > cost:
    res = profit / cost
    print("Profitability: {}".format(res))
elif profit < cost:
    print("You work in the negative")
else:
    print("So, it's like a ZERO or MISTAKE")
