# Task 6

a = int(input("Enter a profit: "))
b = int(input("Enter a cost: "))
res = 1

d = a * 1.1

while d < b:
    d = d * 1.1
    res +=1

print("On the {} day".format(res))
