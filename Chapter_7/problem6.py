# 6. Write a program to calculate the factorial of a given number using for loop. 

fac = 1
n = int(input("Enter a number to get its factorial : "))

for i in range (1,n+1):
    fac = fac * i

if(n<0):
        print("invalid number")
else:
    print(f"the fac of the {n} is {fac}")