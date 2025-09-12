# 4. Write a program to find whether a given number is prime or not.

n = int(input("Enter a number to get its nature : "))

for i in range (1,n+1):
    if n%2 == 0 and n != 2:
        print(f"the number {n} is not Prime")
        break
    else:
        print(f"the number {n} is Prime")
        break
        