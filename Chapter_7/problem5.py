# 5. Write a program to find the sum of first n natural numbers using while loop.

sum = 0
n = int(input("Enter a number to get its SUM : "))

for i in range (n+1):
    sum = sum + i

print(f"the sum of the {n} is {sum}")