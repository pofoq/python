# Task 4

n = input("Enter a number: ")
res = int(n[0])
i = 1
while i < len(n):
    if int(n[i]) > res:
        res = int(n[i])
    i += 1

print("The bigest number is {}".format(res))
