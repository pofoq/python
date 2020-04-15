# Task 4

n = int(input("Enter a number: "))
ln = 1
d = n % 10
n = n // 10
num_max = d

while n > 0:
    n = n // 10
    d = n % 10
    if num_max < d:
        num_max = d
    if num_max == 9:
        break

print("Max number is {}".format(num_max))

